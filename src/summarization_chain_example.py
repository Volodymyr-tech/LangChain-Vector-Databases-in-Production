from dotenv import load_dotenv
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate

from langchain_openai import ChatOpenAI
import os

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, api_key=API_KEY)

# Load the summarization chain
summarize_chain = load_summarize_chain(llm)

# Load the document using PyPDFLoader
document_loader = PyPDFLoader(file_path="../data_ex.pdf")
document = document_loader.load()
print(document)
# Summarize the document
summary = summarize_chain.invoke(document)
print(summary["output_text"])
