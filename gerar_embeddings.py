import numpy as np
from langchain_community.embeddings import OllamaEmbeddings

# Códigos de cores ANSI para texto
GREEN = "\033[92m"
RESET = "\033[0m"  # Reset para a cor padrão

# Definir os documentos (ou frases)
documents = [
    "Redes Neurais em Python: introdução ao uso de bibliotecas como TensorFlow e PyTorch.",
    "Machine Learning com Python: como usar bibliotecas como Scikit-learn para criar modelos preditivos."
]

# Inicializando o modelo de embeddings do Ollama
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Gerando os embeddings para os documentos
document_embeddings = embeddings.embed_documents(documents)

# Mostra o tamanho de cada embedding (dimensão)
embedding_size = len(document_embeddings[0])
print(f"{GREEN}Tamanho de cada embedding (Dimensão):{RESET} {embedding_size}")

# Mostra a quantidade total de embeddings gerados
num_embeddings = len(document_embeddings)
print(f"{GREEN}Quantidade total de embeddings gerados:{RESET} {num_embeddings}")



# Exibindo os vetores de embeddings gerados para cada documento
for idx, embedding in enumerate(document_embeddings):
    print(f"{GREEN}Embedding para o documento {idx + 1}:{RESET} {embedding}")