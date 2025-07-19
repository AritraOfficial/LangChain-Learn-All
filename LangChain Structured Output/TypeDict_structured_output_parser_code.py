from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
# from typing import TypedDict
from typing import TypedDict, Annotated

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash')

# =============================================
#Schema for structured output
class Review(TypedDict):
    summary: Annotated[str, "A Brief summary of the review."]
    sentiment: Annotated[str, "Return sentiment of the review either - negative, position"]
# =============================================
structured_model = model.with_structured_output(Review)

result = structured_model.invoke (""" The hardware is great, but the software feels bloated. 
                    There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared
                    to other brands. Hoping for a software update to fix this.""")

print(result)


#not not - giving type error - using google generative ai for that