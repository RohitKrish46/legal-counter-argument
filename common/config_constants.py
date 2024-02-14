from common.utils import read_config_file
config = read_config_file()

config_openai = config["openai"]
OPEN_AI_API_KEY = config_openai['apikey']

config_pinecone = config["pinecone"]
PINCEONE_API_KEY = config_pinecone['apikey']
INDEX_NAME = config_pinecone['index_name']
ENVIRONMENT = config_pinecone['environment']


config_data_dir = config["data_dir"]
DATA_PATH = config_data_dir['path']