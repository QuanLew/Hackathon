# CMPE 172 Hackathon - Chatbot - Food Security 2023

## Requirements
- [Ollama](https://ollama.ai/) verson 0.1.26 or higher.

## Setup
1. Clone this repository to your local machine.
2. Create a Python virtual environment by running `python3 -m venv .venv`.
3. Activate the virtual environment by running `source .venv/bin/activate` on Unix or MacOS, or `.\.venv\Scripts\activate` on Windows.
4. Install the required Python packages by running `pip install -r requirements.txt`.

## Running the Project
**Note:** The first time you run the project, it will download the necessary models from Ollama for the LLM and embeddings. This is a one-time setup process and may take some time depending on your internet connection.

1. Ensure your virtual environment is activated.
2. Run the main script with `python app.py`.
3. Navigate to `localhost:5000`.
4. Once done, run `Ctrl + C` to terminate the process and run `deactivate` to stop the virtual environment.

This will load the PDFs and Markdown files, generate embeddings, query the collection, and answer the question defined in `app.py`.

## Technologies Used
- [Langchain](https://github.com/langchain/langchain): A Python library for working with Large Language Model
- [Ollama](https://ollama.ai/): A platform for running Large Language models locally.
- [Chroma](https://docs.trychroma.com/): A vector database for storing and retrieving embeddings.
- [PyPDF](https://pypi.org/project/PyPDF2/): A Python library for reading and manipulating PDF files.

## Reference
- [local-LLM-with-RAG](https://github.com/amscotti/local-LLM-with-RAG)