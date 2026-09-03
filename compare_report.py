from langchain_groq import ChatGroq
from utils.config import GROQ_API_KEY
from llm.prompts import COMPARE_REPORTS_PROMPT

llm = ChatGroq(
    model_name="openai/gpt-oss-20b",
    groq_api_key=GROQ_API_KEY,
    temperature=0.2
)


def compare_reports(old_report, new_report):

    response = llm.invoke(
        COMPARE_REPORTS_PROMPT.format(
            old_report=old_report,
            new_report=new_report
        )
    )

    return response.content