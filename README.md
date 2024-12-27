# Instruções para Execução do Script

Este repositório contém um script Python que utiliza a biblioteca `langchain_community` para gerar embeddings a partir de um conjunto de documentos, utilizando o modelo `mxbai-embed-large` da plataforma Ollama. Abaixo estão as orientações para configurar o ambiente, instalar as dependências necessárias e executar o código.

## Pré-requisitos

Antes de executar o script, verifique se você tem as seguintes dependências instaladas e configuradas no seu ambiente:

### 1. **Ollama**
   - **Ollama** é uma plataforma de modelos de linguagem. Você precisará configurar o Ollama para rodar o modelo `mxbai-embed-large`, utilizado para gerar os embeddings no script.
   - **Configuração do Ollama**:
     - Acesse o [site oficial do Ollama](https://ollama.com) para instruções de instalação.
     - Após a instalação, certifique-se de que o modelo `mxbai-embed-large` esteja disponível e acessível em seu ambiente (ollama run mxbai-embed-large). 
### 2. **Python**
   - O script foi desenvolvido para Python. Caso não tenha o Python instalado, faça o download e instalação através do [site oficial do Python](https://www.python.org).

### 3. **pip (gerenciador de pacotes do Python)**
   - Certifique-se de ter o `pip` instalado para gerenciar as dependências do projeto. Caso não tenha o `pip` instalado, você pode seguir as instruções [aqui](https://pip.pypa.io/en/stable/installation/).

### 4. **Dependências Python**
   O script depende de algumas bibliotecas que precisam ser instaladas. Elas são:

   - **numpy**: Utilizado para manipulação de arrays e operações matemáticas.
   - **langchain_community**: Biblioteca usada para gerar os embeddings utilizando o modelo Ollama.

   Para instalar essas dependências, siga os passos abaixo.

No terminal:

   -pip install numpy langchain_community

Após instalação das dependencias, execute o código.
