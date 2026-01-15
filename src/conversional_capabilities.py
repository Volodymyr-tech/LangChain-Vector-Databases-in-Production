import os

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of France?"),
    AIMessage(content="The capital of France is Paris.")
]


prompt = HumanMessage(
    content="I'd like to know more about the city you just mentioned."
)
# add to messages
messages.append(prompt)

llm = ChatOpenAI(model_name="gpt-4", api_key=API_KEY,)

response = llm.invoke(messages)
print(response.content)