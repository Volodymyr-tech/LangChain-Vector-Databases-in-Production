from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

import os

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")


chat = ChatOpenAI(
    api_key=API_KEY, model_name="gpt-4o-mini", temperature=0
)  # creating an instance of chat

template = "You are an assistant that helps users find information about movies."  # determination of template for system
system_message_prompt = SystemMessagePromptTemplate.from_template(
    template
)  # set the system template what our agent will do

human_template = (
    "Find information about the movie {movie_title}."  # what we ask model to do
)

human_message_prompt = HumanMessagePromptTemplate.from_template(
    human_template
)  # question from user that model will answer to

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)  # set templates into the structured dialog with the model

response = chat.invoke(
    chat_prompt.format_prompt(movie_title="Inception").to_messages()
)  # using {movie_title} in human template allow us to add name of movie in the prompt. Using the to_messages object in LangChain allows you to convert the formatted value of a chat prompt template into a list of message objects.

print(response.content)
