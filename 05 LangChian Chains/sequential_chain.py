from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="deepseek-r1-distill-llama-70b")

prompt1 = PromptTemplate(
    template='Generate TOP 5 most asking questions in interviews about {topic} and write all of this in format like - write the question then \n write the answer in short and direct with the main highlights. Then after the one question with answer write \n =============-- \n then write the next question with answer in the same format. \n\n',
    input_variables=['topic']
)

p2 = PromptTemplate(
    template='Write in details with code on {text} and write all of this in format like - write the answer in short and direct with the main highlights \n then the code in python. Then after the one question with answer write \n =============-- \n then write the next question with answer in the same format. \n\n',
    input_variables=['text']
)
parser = StrOutputParser()

chain = prompt1 | model | parser | p2 | model | parser

result = chain.invoke({'topic':'RAG (Retrieval Augmented Generation)'})

print(result)

chain.get_graph().print_ascii()