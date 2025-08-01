from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0")

user_input = input("Enter your query:  ")
result = llm.invoke(user_input)
print("Your query :", user_input, "\nResult:", result)
 