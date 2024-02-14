import os
import openai
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from common.config_constants import OPEN_AI_API_KEY, DATA_PATH

# initializations
os.environ['OPENAI_API_KEY'] = OPEN_AI_API_KEY
openai.api_key = OPEN_AI_API_KEY
directory = DATA_PATH
legal_file = "File's name for which you wanna create counter arguments for"

# load the GPT model
llm = ChatOpenAI(temperature=0.0)

# load a PDF file 
pdf_file_path = f"./{DATA_PATH}/{legal_file}"
loader = PyPDFLoader(pdf_file_path)
docs_raw = loader.load()

# get raw text from doc and split it into chunks of size 2000
docs_raw_text = [doc.page_content for doc in docs_raw]
text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=300)

# create doc for each chunk
docs = text_splitter.create_documents(docs_raw_text)

# prompt to summarize the legal document using PromptTemplate
custom_prompt = """Summarize the following legal document into a max of 10 bullet points: \n\n" + "legal document: {text}"""
PROMPT = PromptTemplate(template=custom_prompt, input_variables=["text"])

# chain the prompt and the summarization text with map reduce chaining
chain = load_summarize_chain(llm, chain_type="map_reduce", map_prompt=PROMPT, combine_prompt=PROMPT)
summary_output = chain({"input_documents": docs}, return_only_outputs=True)['output_text']

# summary of document
print(f'\nSummary of the Document:\n{summary_output}')

# prompt to dismiss arguments raised in the legal document
dismiss_prompt = f"Generate some points to dismiss the arguments from the summary of a Legal document: \n\n + legal document summary: {summary_output}"
result = openai.Completion.create(
    model="text-davinci-003",
    prompt=dismiss_prompt,
    max_tokens=1000,
    temperature=0.2,
    top_p=1,
    n=1,
)

# legal counter arguments
print(f'{result["choices"][0]["text"]}')
