from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableParallel 
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model1 = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0.7)
model2 = ChatGroq(model='mistral-saba-24b')

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='The sentiment of the feedback text')
    
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables = {'format_instructions': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model2 | parser2

print(classifier_chain.invoke({'feedback': 'The new features of this product are type of things which are going with, the similarity is ok but like that!'}))