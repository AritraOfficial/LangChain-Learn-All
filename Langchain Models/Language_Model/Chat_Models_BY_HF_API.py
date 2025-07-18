import os   
from dotenv import load_dotenv
load_dotenv()
os.environ["HUGGINGFACE_API_TOKEN"] = "HUGGINGFACE_API_TOKEN"
from huggingface_hub import login
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
os.environ["HF_HOME"] = "D:/Software/huggingface_cache"

llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    # repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

user_input = input("Enter your query:  ")
result = model.invoke(user_input)
print("Your query :", user_input, "\nResult:", result.content)
# result = model.invoke("What is the largest city in the India?")
# print(result.content)
