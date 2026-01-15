from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

from config.base import llm


class ChainPrompting:
    model = llm.chat

