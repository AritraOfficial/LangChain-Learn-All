from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07")

result = model.embed_query("Mumbai is the largest city in India?")

print(str(result))