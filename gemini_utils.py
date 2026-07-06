import os
from dotenv import load_dotenv
from google import genai
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Read API key from .env
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini client
client = genai.Client(api_key=API_KEY)


def get_ai_analysis(resume_text, job_description):

    template = """
    You are an expert career advisor.

    Analyze the following resume and job description.

    Resume:
    {resume}

    Job Description:
    {job_description}

    Provide:
    1. Candidate Strengths
    2. Candidate Weaknesses
    3. Career Suggestions
    4. Learning Roadmap

    Keep the response clear and professional.
    """

    prompt_template = PromptTemplate(
        input_variables=["resume", "job_description"],
        template=template
    )

    prompt = prompt_template.format(
        resume=resume_text,
        job_description=job_description
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text