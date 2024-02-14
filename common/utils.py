import warnings
warnings.filterwarnings("ignore")
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import yaml


def read_config_file():
    """
    Read the config.yaml file

    """
    with open(f"config/config.yaml") as file:
        config_data = yaml.safe_load(file)
    return config_data



# to load all documents from a directory
def load_docs(directory):
  loader = PyPDFLoader(directory)
  documents = loader.load()
  return documents


# chunk up the documents
def split_docs(documents, chunk_size=1000, chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

# Get similar document based on a query
def get_similiar_docs(index, query, k=2, score=False):
  if score:
    similar_docs = index.similarity_search_with_score(query, k=k)
  else:
    similar_docs = index.similarity_search(query, k=k)
  return similar_docs


# Get relevant answers and reply back with LLM
def get_answer(index, chain, query):
  similar_docs = get_similiar_docs(index, query)
  answer = chain.run(input_documents=similar_docs, question=query)
  return answer
