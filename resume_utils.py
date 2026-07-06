import pdfplumber


def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_skills(text):

    skills_list = [
        "python", "java", "c", "c++", "sql",
        "machine learning", "deep learning",
        "data science", "artificial intelligence",
        "html", "css", "javascript",
        "react", "angular", "node.js",
        "mongodb", "mysql", "postgresql",
        "git", "github", "docker", "kubernetes",
        "aws", "azure", "gcp",
        "streamlit", "flask", "django",
        "tensorflow", "pytorch", "keras",
        "numpy", "pandas", "scikit-learn",
        "power bi", "tableau", "excel",
        "nlp", "opencv", "langchain",
        "faiss", "rag", "llm"
    ]
    found_skills = []

    text = text.lower()

    for skill in skills_list:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))

def find_missing_skills(resume_skills, job_description):

    job_description = job_description.lower()

    required_skills = []

    skills_list = [
        "python", "java", "c", "c++", "sql",
        "machine learning", "deep learning",
        "data science", "artificial intelligence",
        "html", "css", "javascript",
        "react", "angular", "node.js",
        "mongodb", "mysql", "postgresql",
        "git", "github", "docker", "kubernetes",
        "aws", "azure", "gcp",
        "streamlit", "flask", "django",
        "tensorflow", "pytorch", "keras",
        "numpy", "pandas", "scikit-learn",
        "power bi", "tableau", "excel",
        "nlp", "opencv", "langchain",
        "faiss", "rag", "llm"
    ]

    for skill in skills_list:
        if skill in job_description:
            required_skills.append(skill)

    missing_skills = list(set(required_skills) - set(resume_skills))

    return missing_skills

def calculate_match_score(resume_skills, job_description):

    job_description = job_description.lower()

    skills_list = [
        "python", "java", "c", "c++", "sql",
        "machine learning", "deep learning",
        "data science", "artificial intelligence",
        "html", "css", "javascript",
        "react", "angular", "node.js",
        "mongodb", "mysql", "postgresql",
        "git", "github", "docker", "kubernetes",
        "aws", "azure", "gcp",
        "streamlit", "flask", "django",
        "tensorflow", "pytorch", "keras",
        "numpy", "pandas", "scikit-learn",
        "power bi", "tableau", "excel",
        "nlp", "opencv", "langchain",
        "faiss", "rag", "llm"
    ]

    required_skills = []

    for skill in skills_list:
        if skill in job_description:
            required_skills.append(skill)

    if len(required_skills) == 0:
        return 0

    matched = len(set(resume_skills) & set(required_skills))

    score = (matched / len(required_skills)) * 100

    return round(score, 2)