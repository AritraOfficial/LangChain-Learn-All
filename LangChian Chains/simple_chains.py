from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from huggingface_hub import login
import os   
os.environ["HF_HOME"] = "D:/Software/huggingface_cache"


os.environ["HUGGINGFACE_API_TOKEN"] = "HUGGINGFACE_API_TOKEN"
load_dotenv()

prompt = PromptTemplate(
    template='Generate TOP 5 most asking questions in interviews about {topic} and write all of this in format like - write the question then \n write the answer in short and direct with the main highlights. Then after the one question with answer write \n =============-- \n then write the next question with answer in the same format. \n\n',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.1)

# model = ChatHuggingFace(llm = (HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")))

parser = StrOutputParser()  

chain = prompt | model | parser

result = chain.invoke({'topic':'RAG (Retrieval Augmented Generation)'})

print(result)

chain.get_graph().print_ascii()