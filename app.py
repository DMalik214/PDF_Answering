from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
from pdf_extractor import extract_text_from_pdf, get_relevant_context
from qa_model import load_glove_embeddings, find_most_similar_sentence

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

embeddings_path = 'glove.6B.100d.txt'
glove_embeddings = load_glove_embeddings(embeddings_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'message': "No selected file"})
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        try:
            file.save(file_path)
            text = extract_text_from_pdf(file_path)
            return jsonify({'success': True, 'message': "File uploaded successfully", 'text': text})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)})

@app.route('/qa')
def qa_page():
    return render_template('qa.html')

@app.route('/answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    context = data.get('context', '')
    question = data.get('question', '')
    relevant_context = get_relevant_context(context, question)
    answer = find_most_similar_sentence(relevant_context.split('. '), question, glove_embeddings)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
