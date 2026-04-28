import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

load_dotenv()

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
CHROMA_DIR = os.path.join(os.path.dirname(__file__), '..', 'chroma_db')

embeddings = SentenceTransformerEmbeddings(model_name="paraphrase-multilingual-MiniLM-L12-v2")

def load_documents():
    docs = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.txt'):
            filepath = os.path.join(DATA_DIR, filename)
            loader = TextLoader(filepath, encoding='utf-8')
            documents = loader.load()
            character = filename.replace('.txt', '')
            for doc in documents:
                doc.metadata['character'] = character
            docs.extend(documents)
    return docs

def build_vectorstore():
    docs = load_documents()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_DIR)
    print("Векторная база создана!")
    return vectorstore

def get_vectorstore():
    if os.path.exists(CHROMA_DIR):
        return Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
    else:
        return build_vectorstore()

def retrieve_context(query: str, character: str, k: int = 5):
    vectorstore = get_vectorstore()

    results = vectorstore.similarity_search(
        query,
        k=k,
        filter={"character": character}
    )

    general_results = vectorstore.similarity_search(
        character,
        k=3,
        filter={"character": character}
    )

    all_docs = results + general_results
    seen = set()
    unique_docs = []
    for doc in all_docs:
        if doc.page_content not in seen:
            seen.add(doc.page_content)
            unique_docs.append(doc)

    context = "\n\n".join([doc.page_content for doc in unique_docs])
    return context