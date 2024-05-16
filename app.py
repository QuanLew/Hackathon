from flask import Flask, render_template, request
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from models import check_if_model_is_available
from document_loader import load_documents
import argparse
import sys

from llm import getChatChain

from flask import Flask, request, jsonify

app = Flask(__name__)

TEXT_SPLITTER = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

def load_documents_into_database(model_name: str, documents_path: str) -> Chroma:
    """
    Loads documents from the specified directory into the Chroma database
    after splitting the text into chunks.

    Returns:
        Chroma: The Chroma database with loaded documents.
    """

    print("Loading documents")
    raw_documents = load_documents(documents_path)
    documents = TEXT_SPLITTER.split_documents(raw_documents)

    print("Creating embeddings and loading documents into Chroma")
    db = Chroma.from_documents(
        documents,
        OllamaEmbeddings(model=model_name),
    )
    return db

# Load documents into the database and check model availability at startup
llm_model_name = 'mistral'
embedding_model_name = 'nomic-embed-text'
documents_path = './Research'

try:
    check_if_model_is_available(llm_model_name)
    check_if_model_is_available(embedding_model_name)
except Exception as e:
    print(f"Error checking model availability: {e}")
    sys.exit(1)

try:
    db = load_documents_into_database(embedding_model_name, documents_path)
    print("Finish loading documents.")
except FileNotFoundError as e:
    print(f"Error loading documents into database: {e}")
    sys.exit(1)

llm = Ollama(model=llm_model_name)
chat = getChatChain(llm, db)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat_handler():
    data = request.get_json()
    user_input = data['input']
    chat_response_local = chat(user_input)
    return jsonify({'response': chat_response_local})

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()