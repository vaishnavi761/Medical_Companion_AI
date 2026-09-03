from langchain_groq import ChatGroq

from utils.config import GROQ_API_KEY
from llm.prompts import TIMELINE_PROMPT

llm = ChatGroq(
    model_name="openai/gpt-oss-20b",
    groq_api_key=GROQ_API_KEY,
    temperature=0.2
)


def generate_timeline(previous_report, current_report):

    response = llm.invoke(
        TIMELINE_PROMPT.format(
            old_report=previous_report,
            new_report=current_report
        )
    )

    return response.content