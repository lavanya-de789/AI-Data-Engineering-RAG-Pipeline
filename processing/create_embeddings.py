from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

loader=PyPDFDirectoryLoader(
'data/raw'
)

docs=loader.load()

splitter=(
RecursiveCharacterTextSplitter(
chunk_size=500,
chunk_overlap=50
)
)

chunks=splitter.split_documents(
docs
)

embeddings=HuggingFaceEmbeddings(
model_name='all-MiniLM-L6-v2'
)

vector_db=FAISS.from_documents(
chunks,
embeddings
)

vector_db.save_local(
'data/vector_store'
)

print('embeddings created')
