from langchain.document_loaders import PyPDFDirectoryLoader

loader=PyPDFDirectoryLoader(
'data/raw'
)

docs=loader.load()

print('documents:',len(docs))
