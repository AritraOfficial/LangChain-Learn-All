from dotenv import load_dotenv 
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm_model = ChatHuggingFace(llm = (HuggingFaceEndpoint(repo_id="google/gemma-2-2b-it", task="text-generation")))
# model = ChatHuggingFace(llm = llm_model)
parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | llm_model | parser

# prompt = template.format()
result = chain.invoke({'topic': 'AI-LLMs'})
print(result)