# legal-counter-argument

A powerful LLM-powered pipeline for summarizing legal documents, generating intelligent counterarguments, and enabling context-aware legal question answering. This system is designed to support individuals in understanding legal documents and crafting robust responses to legal accusations.

📌 Table of Contents
- [🧩 Overview](#-overview)

- [⚙️ Features](#-features)

- [📐 System Architecture](#-system-architecture)

    [1. Document Summarization & Counter-Argument Generation Workflow](#-1-document-summarization--counter-argument-generation-workflow)
  
    [2. Document Question Answering Workflow](#2-document-question-answering-workflow)

- [🚀 Quick Start](#-quick-start)

- [📌 Future Enhancements](#-future-enhancements)


## 🧩 Overview
This project aims to empower users to generate intelligent legal counterarguments and ask detailed questions about legal documents using large language models (LLMs) like OpenAI’s gpt-3.5-turbo. It supports legal professionals, individuals without legal expertise, and researchers who need automated assistance with legal content.

## ⚙️ Features
- ✔️ Automatic summarization of lengthy legal documents
- ✔️ Counter-argument generation using LLMs
- ✔️ Multi-format document ingestion (PDF, HTML, TXT)
- ✔️ Semantic search & question-answering with Pinecone vector store
- ✔️ LangChain-powered modular pipelines for flexibility and scalability

## 📐 System Architecture


### 🔁 1. Document Summarization & Counter-Argument Generation Workflow:

1. Input Parsing: Load large legal documents from various formats.

2. Chunking: Split into overlapping chunks (~2000 tokens) for contextual coherence.

3. Prompt Design: Use custom prompt templates tailored for legal summarization.

4. LLM Summarization: Generate summary chunks using load_summarize_chain from LangChain.

5. Summary Fusion: Combine individual summaries into a final, cohesive summary.

6. Counter-Argument Generation: Use OpenAI’s GPT models to derive intelligent counterarguments from the final summary.

![image](https://github.com/RohitKrish46/legal-counter-argument/assets/25106707/cf70f0f1-35dc-4fb4-a8b9-ff45324b09f8)


## 🔁 2. Document Question Answering Workflow


1. Multi-format Support: Ingest files in PDF, text, or HTML format.

2. Recursive Chunking: Segment using RecursiveCharacterTextSplitter (~1000 tokens with overlap).

3. Embedding: Create dense vector embeddings using OpenAI's text-embedding-ada-002.

4. Vector Store Setup: Store vectors in Pinecone for semantic search.

5. QA Chain: Use LangChain’s load_qa_chain to retrieve relevant content and generate answers from LLM.

![image](https://github.com/RohitKrish46/legal-counter-argument/assets/25106707/6031de06-d689-49dd-86e5-05d1c8e55f9e)


## 🚀 Quick Start

### 🔧 Prerequisites
- Python 3.9+
- OpenAI API key
- Pinecone API key & environment setup

### 📦 Installation
```
git clone https://github.com/yourusername/legal-counter-argument.git
cd legal-counter-argument
pip install -r requirements.txt
```
### ⚙️ Configuration
Update your .env file or set environment variables for:
```
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_environment
```
### 🏃‍♂️ Running the Pipeline
```
# Run summarization & counter-argument generation
python summarize_and_counterarg.py --input_dir ./legal_docs

# Run document QA setup
python qa_pipeline.py --input_dir ./legal_docs

# Ask a question
python ask_question.py --question "What are the key charges in the document?"
```
## 📌 Future Enhancements
- 🔒 Integrate document redaction for sensitive information

- 🌐 Add support for multilingual legal documents

- 🧠 Fine-tune smaller local LLMs for on-premise deployment

- 📊 Visual dashboard for document navigation and QA
