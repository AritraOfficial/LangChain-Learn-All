from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-1.5-flash")

user_input = input("Enter your query:  ")
result = llm.invoke(user_input)
print("Your query :", user_input, "\nResult:", result)