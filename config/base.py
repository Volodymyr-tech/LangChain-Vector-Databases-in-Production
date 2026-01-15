from langchain_openai import ChatOpenAI

from config.config_llm import chat_config



class LlmModel:

    def __init__(self, api_key):
        self.chat = ChatOpenAI(
            api_key=api_key, model_name="gpt-4o-mini", temperature=0
        )  # creating an instance of chat


llm = LlmModel(api_key=chat_config.OPENAI_API_KEY)
