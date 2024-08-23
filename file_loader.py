import ssl
from langchain_community.document_loaders import UnstructuredPDFLoader
ssl._create_default_https_context = ssl._create_unverified_context

def get_content(file_path):
    loader = UnstructuredPDFLoader(file_path)
    data = loader.load()
    return data[0].page_content