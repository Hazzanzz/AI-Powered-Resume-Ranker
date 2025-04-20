import openai
import os
from secrets import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY


def suggest_resume_improvements(resume_text: str, job_description: str) -> str:
    """
    Uses OpenAI's GPT to analyze and suggest improvements to the resume
    based on the job description.
    """
    prompt = f"""
You are a helpful HR assistant.

Below is a candidate's resume and a job description. Provide actionable, professional suggestions on how the resume can be improved to better fit the job.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Suggestions:
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are an expert HR consultant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response['choices'][0]['message']['content'].strip()
