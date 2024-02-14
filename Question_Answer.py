import os
import warnings
warnings.filterwarnings("ignore")
import openai
import pinecone
from langchain.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import Pinecone
from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain
from common.utils import load_docs, get_similiar_docs, split_docs, get_answer
from common.config_constants import OPEN_AI_API_KEY, DATA_PATH, PINCEONE_API_KEY, INDEX_NAME, ENVIRONMENT


os.environ['OPENAI_API_KEY'] = OPEN_AI_API_KEY
directory = DATA_PATH
file = 'Transformers.pdf'


# Step 1: Get all documents from data folder and chunk them
documents = PyPDFLoader(directory)
docs = split_docs(documents)
print(f'Total numbner of documnents: {len(documents)}')
print(f'Total numbner of documnents after Chunking: {len(docs)}')

# # Step 2: Embed your chunked data
embeddings = OpenAIEmbeddings(model_name="ada")

# check embedding dimensions
query_result = embeddings.embed_query("wubba lubba dub dub")
print(f'Dimensions of Embedding for a sample text: {len(query_result)}')


#Step 3: Store embeded data in pinecone
pinecone.init(
    api_key=PINCEONE_API_KEY,
    environment= ENVIRONMENT
)

index_name = INDEX_NAME
index = Pinecone.from_documents(docs, embeddings, index_name=index_name)

# if you have already indexed the doc, uncomment this and use
# index = Pinecone.from_existing_index(index_name, embeddings)

# test to get data from pinecone
query = 'What is the rule of reason?'
similar_docs = get_similiar_docs(index, query, k=3, score=True)
print(similar_docs)

# load GPT model
model_name = "gpt-3.5-turbo"
llm = OpenAI(model_name=model_name)
chain = load_qa_chain(llm, chain_type="stuff")


query = 'How encoder and decoder works in Transformers?'
answer = get_answer(index, chain, query)
print(f'Question: {query}\n')
print(f'Ans: {answer}\n')
