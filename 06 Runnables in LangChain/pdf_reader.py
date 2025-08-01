from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "qwen/qwen3-32b")
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Load Document 
loader = TextLoader('docs.txt')
documents = loader.load()

# Split the text into smaller chunks 
text_slitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap =50)
docs = text_slitter.split_documents(documents)

vectorstore = FAISS.from_documents(docs, embedding_model)

retriever = vectorstore.as_retriever()

# query = "What are the key take ways from the documents?"
query = "Write the 4 lines summary of the documents?"
retriever_docs = retriever.get_relevant_documents(query)

retrieved_text = "\n".join([doc.page_content for doc in retriever_docs])

prompt = f"Based on following text, answer the question : {query}\n\n{retrieved_text}"
answer = model.invoke(prompt)

print("--------------------------------------------------------------------\nAnswer: ", answer.content)