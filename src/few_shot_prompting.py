from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

from config.base import llm


class FewShotPrompting:
    model = llm.chat
    examples = [
        {"color": "red", "emotion": "passion"},
        {"color": "blue", "emotion": "serenity"},
        {"color": "green", "emotion": "tranquility"},
    ]

    example_formatter_template = """
    Color: {color}
    Emotion: {emotion}\n
    """
    example_prompt = PromptTemplate(
        input_variables=["color", "emotion"],
        template=example_formatter_template,
    )

    few_shot_prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix="Here are some examples of colors and the emotions associated with them:\n\n",
        suffix="\n\nNow, given a new color, identify the emotion associated with it:\n\nColor: {input}\nEmotion:",
        input_variables=["input"],
        example_separator="\n",
    )

    chain = few_shot_prompt | model

    @classmethod
    def get_response(cls, input_data:dict):
        response = cls.chain.invoke(input_data)
        print("AI-generated", response.content)


if __name__ == "__main__":
    start = FewShotPrompting.get_response(input_data={"input": "purple"})
