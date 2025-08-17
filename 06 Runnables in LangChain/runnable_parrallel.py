from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template= "Generate a X post {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template= "Generate a LinkedIn post {topic}",
    input_variables=["topic"]
)

model = ChatGroq(model="deepseek-r1-distill-llama-70b")

parser = StrOutputParser()

# ===================================================================
parallel_chain = RunnableParallel({
     'tweet': RunnableSequence(prompt1, model, parser),
     'linkedin' : RunnableSequence(prompt2, model, parser)
})
# ===================================================================

result = parallel_chain.invoke({'topic': 'AI'})

print(result['tweet'])
print("-----")
print(result['linkedin'])