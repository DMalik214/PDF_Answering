import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from text_preprocessor import preprocess_text

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text("text")  
    return text

def get_relevant_context(text, question, top_n=3):
    sentences = text.split('. ')
    preprocessed_sentences = [preprocess_text(sentence) for sentence in sentences]
    vectorizer = TfidfVectorizer().fit_transform(preprocessed_sentences + [preprocess_text(question)])
    vectors = vectorizer.toarray()
    
    cosine_similarities = cosine_similarity(vectors[-1:], vectors[:-1])
    similar_indices = cosine_similarities.argsort().flatten()[-top_n:]
    relevant_sentences = [sentences[i] for i in similar_indices]
    return ' '.join(relevant_sentences)

if __name__ == "__main__":
    pdf_path = "sample.pdf"  # Replace with your PDF file path
    text = extract_text_from_pdf(pdf_path)
    question = "What is the main topic?"
    context = get_relevant_context(text, question)
    print(context)
