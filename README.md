# Sistema de Recuperação de Informações com FAISS e RetrievalQA

## 1. Descrição do Projeto

Este projeto foi desenvolvido como parte da atividade da Unidade 5 do curso de Sistemas para Internet.

O objetivo é construir um sistema de Recuperação de Informações (RAG - Retrieval-Augmented Generation) utilizando embeddings, um banco de dados vetorial e um modelo de linguagem local.

O sistema permite que o usuário faça perguntas sobre um conjunto de textos previamente carregados. A aplicação recupera os trechos mais relevantes do conteúdo e utiliza um modelo de linguagem para gerar respostas contextualizadas.

## 2. Tecnologias Utilizadas

- **Python 3.12:** linguagem de programação utilizada no desenvolvimento.
- **LangChain:** framework para integração dos componentes de recuperação e geração de respostas.
- **FAISS:** banco de dados vetorial utilizado para armazenar e buscar embeddings.
- **Ollama:** ferramenta para execução local de modelos de inteligência artificial.
- **mxbai-embed-large:** modelo utilizado para gerar embeddings dos textos e das perguntas.
- **llama3.2:** modelo de linguagem utilizado para gerar respostas.
- **TextLoader:** componente responsável pelo carregamento do arquivo de texto.
- **RecursiveCharacterTextSplitter:** ferramenta utilizada para dividir o conteúdo em chunks.

## 3. Estrutura do Projeto

```text
atividadeU5/
├── dados.txt
├── main.py
├── requirements.txt
└── README.md
```

- `dados.txt`: arquivo contendo os textos utilizados como base de conhecimento.
- `main.py`: código-fonte responsável pelo carregamento dos documentos, geração dos embeddings, criação do banco FAISS e execução do RetrievalQA.
- `requirements.txt`: lista das dependências Python necessárias.
- `README.md`: documentação do projeto.

## 4. Pré-requisitos

Antes de executar o projeto, é necessário instalar:

- Python 3.12.
- Ollama.

Também é necessário ter os modelos utilizados pelo projeto disponíveis no Ollama:

- mxbai-embed-large.
- llama3.2

## 5. Instalação e Configuração

### 5.1. Criar o ambiente virtual

No Windows, execute:

```powershell
python -m venv venv
```

Ative o ambiente virtual:

```cmd
venv\Scripts\activate
```

### 5.2. Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

As bibliotecas utilizadas estão especificadas no arquivo `requirements.txt`.

### 5.3. Instalar e configurar o Ollama

O Ollama pode ser obtido em:

https://ollama.com/download

Após a instalação, abra o terminal e baixe os modelos necessários:

```bash
ollama pull mxbai-embed-large
```

```bash
ollama pull llama3.2:latest
```

O primeiro modelo será utilizado para gerar os embeddings, enquanto o segundo será responsável pela geração das respostas.

Certifique-se de que o Ollama esteja em execução antes de iniciar a aplicação.

Para verificar os modelos instalados:

```bash
ollama list
```

## 6. Execução do Projeto

Com o ambiente virtual ativado e o Ollama em execução, acesse a pasta do projeto e execute:

```bash
python main.py
```

Durante a inicialização, o sistema realiza as seguintes operações:

1. Carrega o conteúdo do arquivo `dados.txt`.
2. Divide os documentos em chunks de até 500 caracteres, com sobreposição de 50 caracteres.
3. Gera embeddings para cada chunk utilizando o modelo `mxbai-embed-large`.
4. Armazena os vetores no banco de dados FAISS.
5. Configura o RetrievalQA para recuperar os três trechos mais relevantes.
6. Aguarda as perguntas do usuário no terminal.

Quando o sistema estiver pronto, será exibida a mensagem:

```text
Sistema pronto! Digite sua pergunta (ou 'sair' para encerrar).
```

Digite uma pergunta relacionada ao conteúdo de `dados.txt`.

Para encerrar a aplicação, digite:

```text
sair
```

## 7. Exemplos de Utilização

Considerando que o arquivo `dados.txt` contenha informações sobre Inteligência Artificial a resposta que obtive foi:

**Pergunta:**
```text
O que é inteligência artificial?
```

**Resposta esperada:**
A inteligência artificial é, de forma genérica, a capacidade de máquinas demonstrarem inteligência, raciocínio e aprendizado de forma semelhante ao pensamento humano.

*Observação: as respostas são exemplos ilustrativos. As respostas reais dependem do conteúdo presente no arquivo `dados.txt` e do modelo utilizado.*

## 8. Funcionamento do Sistema

O fluxo de funcionamento pode ser representado da seguinte maneira:

```text
Arquivo dados.txt
       |
       v
Carregamento dos documentos
       |
       v
Divisão em chunks
       |
       v
Geração dos embeddings
       |
       v
Armazenamento no FAISS
       |
       v
Pergunta do usuário
       |
       v
Embedding da pergunta
       |
       v
Busca dos chunks mais relevantes
       |
       v
RetrievalQA + modelo Llama 3.2
       |
       v
Resposta contextualizada
```

O FAISS realiza a busca por similaridade vetorial, enquanto o RetrievalQA integra a recuperação dos documentos com o modelo de linguagem.
