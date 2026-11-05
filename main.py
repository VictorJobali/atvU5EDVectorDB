from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama.llms import OllamaLLM
from langchain.chains import RetrievalQA

# ---------------------------------------------------------
# ETAPA 1: Carregar o texto
# ---------------------------------------------------------
loader = TextLoader("dados.txt", encoding="utf-8")
documentos = loader.load()
print(f"Documentos carregados: {len(documentos)}")

# ---------------------------------------------------------
# ETAPA 2: Dividir o texto em chunks
# ---------------------------------------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    length_function=len,
)
chunks = text_splitter.split_documents(documentos)
print(f"Quantidade de chunks: {len(chunks)}")

# ---------------------------------------------------------
# ETAPA 3: Gerar embeddings e inserir no FAISS
# ---------------------------------------------------------
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
db = FAISS.from_documents(chunks, embeddings)
print("Embeddings gerados e inseridos no FAISS.")
print("Quantidade de vetores no FAISS:", db.index.ntotal)

# ---------------------------------------------------------
# ETAPA 4: Configurar o RetrievalQA
# ---------------------------------------------------------
modelo = OllamaLLM(model="llama3.2:latest")
retriever = db.as_retriever(search_kwargs={"k": 3})

qa_chain = RetrievalQA.from_chain_type(
    llm=modelo,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True,
)

# ---------------------------------------------------------
# ETAPA 5: Loop de perguntas
# ---------------------------------------------------------
print("\nSistema pronto! Digite sua pergunta (ou 'sair' para encerrar).\n")

while True:
    pergunta = input("Pergunta: ").strip()
    if pergunta.lower() in ("sair", "exit", "quit"):
        break
    if not pergunta:
        continue

    resultado = qa_chain.invoke(pergunta)
    print("\nResposta:", resultado["result"])
    print("\n--- Trechos usados ---")
    for i, doc in enumerate(resultado["source_documents"], 1):
        print(f"[{i}] {doc.page_content[:150]}...")
    print()