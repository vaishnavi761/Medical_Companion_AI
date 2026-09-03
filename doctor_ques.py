from langchain_groq import ChatGroq

from utils.config import GROQ_API_KEY
from llm.prompts import DOCTOR_QUESTIONS_PROMPT

llm = ChatGroq(
    model_name="openai/gpt-oss-20b",
    groq_api_key=GROQ_API_KEY,
    temperature=0.2
)


def generate_doctor_questions(
    current_report,
    previous_report=""
):

    response = llm.invoke(
        DOCTOR_QUESTIONS_PROMPT.format(
            current_report=current_report,
            previous_report=previous_report
        )
    )

    return response.content