from langchain_groq import ChatGroq
from utils.config import GROQ_API_KEY
from llm.prompts import (
    SUMMARY_PROMPT,
    MEDICINE_PROMPT,
    DIAGNOSIS_PROMPT,
    LAB_PROMPT,
    LIFESTYLE_PROMPT,
)

llm = ChatGroq(
    model_name="openai/gpt-oss-20b",
    groq_api_key=GROQ_API_KEY,
    temperature=0.2,
)

def summarize_report(text):
    response = llm.invoke(
        SUMMARY_PROMPT.format(text=text)
    )
    return response.content


def explain_medicines(text):
    response = llm.invoke(
        MEDICINE_PROMPT.format(text=text)
    )
    return response.content


def explain_diagnosis(text):
    response = llm.invoke(
        DIAGNOSIS_PROMPT.format(text=text)
    )
    return response.content


def explain_lab_tests(text):
    response = llm.invoke(
        LAB_PROMPT.format(text=text)
    )
    return response.content


def lifestyle_tips(text):
    response = llm.invoke(
        LIFESTYLE_PROMPT.format(text=text)
    )
    return response.content