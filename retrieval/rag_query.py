from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

embeddings=HuggingFaceEmbeddings(
model_name='all-MiniLM-L6-v2'
)

store=FAISS.load_local(
'data/vector_store',
embeddings,
allow_dangerous_deserialization=True
)

query='What are the main skills for data engineering?'

results=store.similarity_search(
query,
k=3
)

for r in results:
    print()
    print(r.page_content)
