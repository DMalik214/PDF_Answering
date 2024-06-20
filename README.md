PDF Answering AI:

imp: A text file named "glove.6B.100d.txt" also need to downloaded for using the model, which is at "https://nlp.stanford.edu/data/glove.6B.zip"

PDF Answering AI
PDF Answering AI is a web-based application that allows users to upload PDF documents, extract their text content, and ask questions about the content. The system leverages natural language processing (NLP) techniques and machine learning models to provide accurate answers to user queries.

Table of Contents:
Features
Installation
Usage
File Structure
Technologies Used




Features:
Upload PDF documents
Extract text content from PDFs
Ask questions about the extracted text
Receive relevant answers based on the extracted content

Installation:
Prerequisites
Python 3.7 or higher
pip (Python package installer)
Clone the Repository
Clone the repository from your GitHub account and navigate to the project directory.
Install Dependencies
Install the necessary dependencies using pip.
Download GloVe Embeddings
Download the GloVe embeddings from the Stanford NLP website and place the glove.6B.100d.txt file in the project directory.

Usage:
Run the Application
Run the application using Python. The application will start and be accessible at http://127.0.0.1:5000.

Uploading a PDF
Open your web browser and go to the URL where the application is running.
On the home page, you will see an option to upload a PDF.
Click on the "Choose File" button, select the PDF file you want to upload, and then click the "Upload" button.
The system will extract the text from the PDF and store it.
Asking Questions
After uploading the PDF, you will be redirected to the question-answering page.
Enter your question in the input field provided and click the "Ask" button.
The system will process your question and provide an answer based on the extracted text.

File Structure
index.html: Frontend for uploading PDF files.
qa.html: Frontend for asking questions.
app.py: Flask application file.
pdf_extractor.py: Contains functions for extracting text from PDFs and retrieving relevant context.
qa_model.py: Contains functions for loading GloVe embeddings and finding the most similar sentence.
text_preprocessor.py: Contains text preprocessing functions.

Technologies Used
Flask: Web framework for Python.
PyMuPDF (fitz): Library for extracting text from PDF files.
scikit-learn: Library for machine learning and text processing.
NLTK: Natural Language Toolkit for text preprocessing.
GloVe: Pre-trained word embeddings.
