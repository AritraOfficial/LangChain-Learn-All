from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model= 'deepseek-r1-distill-llama-70b')
parser = StrOutputParser()
prompt = PromptTemplate(template="Write a joke about {topic}", input_variables=['topic'])

joke_gen_chain = RunnableSequence(prompt, model, parser)


def word_count(text):
    return len(text.split())

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({"topic": "RAG"}))
