from dotenv import load_dotenv
from langchain_classic.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate

from langchain_openai import ChatOpenAI
import os

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

prompt = PromptTemplate(template="Question: {question}\nAnswer:", input_variables=["question"])

llm = ChatOpenAI(api_key=API_KEY, model_name="gpt-4o-mini", temperature=0)
chain = prompt | llm

response = chain.invoke("what is the meaning of life?")
print(response)