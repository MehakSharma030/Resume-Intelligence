# 📄 Resume Intelligence

An AI-powered Resume Intelligence System that analyzes resumes against job descriptions to provide resume matching, ATS score prediction, skill analysis, and personalized AI-powered career recommendations.

---

## 🚀 Project Overview

Resume Intelligence is an intelligent resume screening application developed using **Python**, **Streamlit**, and **Google Gemini AI**.

The application helps job seekers evaluate their resumes by comparing them with a given job description and generating detailed insights that can improve their chances of getting shortlisted.

---

## ✨ Features

- 📄 Upload Resume (PDF)
- 💼 Upload Job Description
- 🎯 Resume Match Score
- 🤖 AI-Powered Resume Analysis
- 📊 ATS Compatibility Score
- 💪 Candidate Strengths
- ⚠️ Candidate Weaknesses
- 📚 Personalized Learning Roadmap
- 💡 Career Suggestions
- 📑 PDF Report Generation
- 📈 Interactive Dashboard using Plotly

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI Model
- Google Gemini 2.5 Flash

### Libraries Used
- Streamlit
- Pandas
- Plotly
- pdfplumber
- python-dotenv
- Google Generative AI SDK
- LangChain PromptTemplate

---

## 📂 Project Structure

```
Resume-Intelligence/
│
├── app.py
├── gemini_utils.py
├── resume_utils.py
├── report_generator.py
├── requirements.txt
├── .gitignore
├── .env
│
├── uploads/
├── example_resume/
├── screenshots/
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/MehakSharma030/Resume-Intelligence.git
```

Navigate to the project folder

```bash
cd Resume-Intelligence
```

Create Virtual Environment

```bash
python -m venv .venv
```

Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```text
GEMINI_API_KEY=YOUR_API_KEY
```

> **Note:** Never upload your `.env` file to GitHub.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📊 Workflow

1. Upload Resume (PDF)
2. Upload Job Description
3. Extract Resume Text
4. Compare Resume with Job Description
5. Calculate Resume Match Score
6. Generate AI Analysis using Gemini
7. Display Dashboard
8. Download PDF Report

---

## 📸 Application Screenshots

### Home Page

(Add Screenshot Here)

---

### Resume Analysis Dashboard

(Add Screenshot Here)

---

### AI Career Suggestions

(Add Screenshot Here)

---

### Generated Report

(Add Screenshot Here)

---

## 📈 Future Enhancements

- Resume Ranking for Multiple Candidates
- Resume Keyword Optimization
- ATS Resume Builder
- Skill Gap Analysis
- Interview Question Generation
- Job Recommendation System
- Multi-language Resume Support
- Resume Parsing using OCR

---

## 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Natural Language Processing (NLP)
- Prompt Engineering
- Google Gemini API Integration
- Streamlit Web Development
- Resume Parsing
- Data Visualization
- AI-Powered Decision Support
- PDF Report Generation

---

## 👩‍💻 Author

**Mehak Sharma**

GitHub:
https://github.com/MehakSharma030

---

## ⭐ If you found this project useful

Please consider giving this repository a **Star ⭐**.
