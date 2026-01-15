from langchain_core.prompts import PromptTemplate

from config.base import llm


class RolePrompting:
    model = llm.chat
    template = """
                As a futuristic robot band conductor, I need you to help me come up with a song title.
                What's a cool song title for a song about {theme} in the year {year}?
                """

    prompt = PromptTemplate(
        input_variables=["theme", "year"],
        template=template,
    )

    chain = prompt | model

    @classmethod
    def get_response(cls, input_data:dict):
        response = cls.chain.invoke(input_data)
        print("Theme: interstellar travel")
        print("Year: 3030")
        print("AI-generated song title:", response.content)


if __name__ == "__main__":
    start = RolePrompting.get_response(input_data={"theme": "interstellar travel", "year": "3030"})
