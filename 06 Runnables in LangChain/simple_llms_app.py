from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model= 'mistral-saba-24b')

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}",
    input_variables=['topic']
)

topic = input("Enter a topic >> ")

formatted_prompt = prompt.format(topic=topic)

chain = formatted_prompt | model | parser

result = chain.predict(formatted_prompt)

print("Generated Blog Title: ", chain)