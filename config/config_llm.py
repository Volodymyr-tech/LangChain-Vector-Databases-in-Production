import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class ChatConfig(BaseModel):
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

chat_config = ChatConfig()