
from report_generator import create_pdf_report
from resume_utils import (
    extract_text_from_pdf,
    extract_skills,
    find_missing_skills,
    calculate_match_score,
)

from gemini_utils import get_ai_analysis

import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os


# ---------------------------
# Recommendation Function
# ---------------------------
def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:
        recommendations.append(
            f"Consider learning {skill.title()} to improve your profile."
        )

    return recommendations


# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Resume Intelligence Platform",
    page_icon="📄",
    layout="wide"
)

# Create uploads folder if not exists
os.makedirs("uploads", exist_ok=True)


# ---------------------------
# Custom CSS
# ---------------------------
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.stButton > button {
    background-color: #2563EB;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    border: none;
}

.stButton > button:hover {
    background-color: #1D4ED8;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------
# Header
# ---------------------------
st.markdown("""
<div style="
background: linear-gradient(90deg,#1E3A8A,#2563EB);
padding:30px;
border-radius:15px;
text-align:center;
color:white;
margin-bottom:20px;">

<h1>📄 Resume Intelligence Platform</h1>

<p style="font-size:20px;">
AI-Powered Resume Evaluation & Skill Gap Discovery
</p>

</div>
""", unsafe_allow_html=True)

st.info(
    "Upload a resume and provide a job description to analyze skill gaps and evaluate candidate suitability."
)


#---------------------------
# sidebar
#---------------------------
with st.sidebar:

    st.markdown(
        """
        <div style="
        background:#1E3A8A;
        padding:20px;
        border-radius:12px;
        color:white;
        text-align:center;
        ">

        <h2>📄 Resume Intelligence</h2>

        <p>Version 1.0</p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 🚀 Workflow")

    st.success("1️⃣ Upload Resume")

    st.success("2️⃣ Paste Job Description")

    st.success("3️⃣ Analyze Resume")

    st.success("4️⃣ Review AI Insights")

    st.success("5️⃣ Download Report")

    st.markdown("---")

    st.markdown("## 🛠 Technologies")

    st.write("✔ Python")

    st.write("✔ Streamlit")

    st.write("✔ Google Gemini")

    st.write("✔ Plotly")

    st.write("✔ Matplotlib")

    st.write("✔ PDFPlumber")

    st.write("✔ ReportLab")

    st.markdown("---")

    st.info("""
Supports

• Resume Parsing

• Skill Extraction

• Skill Gap Detection

• AI Career Analysis

• PDF Report Generation
""")

# ---------------------------
# Upload Section
# ---------------------------
st.header("📤 Upload Resume")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

skills = []
resume_text = ""

if uploaded_file is not None:

    save_path = f"uploads/{uploaded_file.name}"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(
        f"Resume '{uploaded_file.name}' uploaded successfully!"
    )
    
    try:
        resume_text = extract_text_from_pdf(save_path)

        skills = extract_skills(resume_text)

    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        st.stop()


    resume_text = extract_text_from_pdf(save_path)

    skills = extract_skills(resume_text)

    st.subheader("🛠 Detected Skills")

    skills_html = ""

    for skill in skills:
        skills_html += f"""
        <span style="
            background-color:#16A34A;
            color:white;
            padding:8px 12px;
            border-radius:15px;
            margin:5px;
            display:inline-block;">
            {skill}
        </span>
        """

    st.markdown(skills_html, unsafe_allow_html=True)

    with st.expander("📄 View Extracted Resume Text"):
        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )


# ---------------------------
# Job Description
# ---------------------------
job_description = st.text_area(
    "Paste Job Description",
    height=200
)


# ---------------------------
# Analyze Button
# ---------------------------
if st.button("🚀 Analyze Resume"):

    if uploaded_file is not None and job_description:

        # Missing Skills
        missing_skills = find_missing_skills(
            skills,
            job_description
        )

        # Match Score
        match_score = calculate_match_score(
            skills,
            job_description
        )

        st.header("📊 Resume Analysis Dashboard")

        # metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "🎯 Match Score",
                f"{match_score}%"
            )

        with col2:
            st.metric(
                "💼 Skills",
                len(skills)
            )

        with col3:
            st.metric(
                "⚠ Missing",
                len(missing_skills)
            )

        with col4:

            if match_score >= 80:
                st.metric(
                    label="Resume Status",
                    value="Excellent ⭐"
                )

            elif match_score >= 60:
                st.metric(
                    label="Resume Status",
                    value="Good 👍"
                )

            else:
                st.metric(
                    label="Resume Status",
                    value="Needs Improvement ⚠️"
                )
        
        # Charts
        col1, col2 = st.columns(2)

        with col1:

            gauge_fig = go.Figure(go.Indicator(

                mode="gauge+number",

                value=match_score,

                title={
                    "text":"<b>Resume Match Score</b>",
                    "font":{"size":22}
                },

                number={
                    "suffix":"%",
                    "font":{"size":40}
                },

                gauge={

                    "axis":{
                        "range":[0,100],
                        "tickwidth":2
                    },

                    "bar":{
                        "color":"#2563EB",
                        "thickness":0.35
                    },

                    "steps":[

                        {
                            "range":[0,40],
                            "color":"#FECACA"
                        },

                        {
                            "range":[40,70],
                            "color":"#FEF08A"
                        },

                        {
                            "range":[70,100],
                            "color":"#BBF7D0"
                        }

                    ],

                    "threshold":{

                        "line":{
                            "color":"red",
                            "width":4
                        },

                        "thickness":0.8,

                        "value":match_score

                    }

                }

            ))

            gauge_fig.update_layout(
                height=300,
                margin=dict(l=20, r=20, t=50, b=20)
            )

            st.plotly_chart(
                gauge_fig,
                use_container_width=True
            )

        with col2:

            matched = max(len(skills) - len(missing_skills), 0)

            pie_fig, ax = plt.subplots(figsize=(4, 4))

            ax.pie(
                [matched, len(missing_skills)],
                labels=["Matched", "Missing"],
                autopct="%1.1f%%",
                startangle=90
            )

            ax.set_title("Skill Match Analysis")

            st.pyplot(pie_fig)

        # Missing Skills
        st.subheader("❌ Missing Skills")

        if missing_skills:

            html = ""

            for skill in missing_skills:
                html += f"""
                <span style="
                background:#F97316;
                color:white;
                padding:8px 12px;
                border-radius:15px;
                margin:5px;
                display:inline-block;">
                {skill}
                </span>
                """

            st.markdown(html, unsafe_allow_html=True)

        else:
            st.success("No missing skills found!")

        # Recommendations
        recommendations = generate_recommendations(
            missing_skills
        )

        st.subheader("💡 Personalized Recommendations")

        for rec in recommendations:

            st.markdown(f"""
            <div style="
                background-color:#F8FAFC;
                border-left:6px solid #2563EB;
                padding:15px;
                border-radius:10px;
                margin-bottom:12px;
                box-shadow:0px 2px 6px rgba(0,0,0,0.1);
            ">
                ✅ {rec}
            </div>
            """, unsafe_allow_html=True)

        # Candidate Report
        st.markdown("---")
        st.subheader("📋 Candidate Analysis Report")

        st.write("### Strengths")

        for skill in skills:
            st.write(f"✅ {skill}")

        st.warning("### ⚠️ Areas for Improvement")

        if missing_skills:
            for skill in missing_skills:
                st.write(f"❌ {skill}")
        else:
            st.success("No improvement areas identified!")

        # Final Recommendation
        st.info("### 🎯 Final Recommendation")

        if match_score >= 80:
            st.success(
                "The candidate is highly suitable for this role."
            )

        elif match_score >= 60:
            st.info(
                "The candidate is moderately suitable but can improve some skills."
            )

        else:
            st.warning(
                "The candidate should improve additional skills before applying."
            )

        # AI Analysis
        st.subheader("🤖 AI Career Analysis")

        with st.spinner("Generating AI insights..."):
            try:
                ai_response = get_ai_analysis(
                    resume_text,
                    job_description
                )

            except Exception as e:
                ai_response = "AI Analysis could not be generated."
                st.error(f"Gemini Error: {e}")

        with st.expander("View AI Career Analysis"):
            st.write(ai_response)

        # PDF Report
        pdf_path = create_pdf_report(
            match_score,
            skills,
            missing_skills,
            recommendations,
            ai_response
        )

        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_file,
                file_name="Resume_Analysis_Report.pdf",
                mime="application/pdf"
            )

        st.success(
            "Resume analysis completed successfully!"
        )

        st.balloons()

    else:
        st.warning(
            "Please upload a resume and enter a job description."
        )


# ---------------------------
# Footer
# ---------------------------
st.markdown("---")

st.markdown("""

<div style="
background:#0F172A;
padding:35px;
border-radius:15px;
color:white;
text-align:center;
margin-top:40px;">

<h2 style="color:white;">
🚀 Resume Intelligence Platform
</h2>

<p style="font-size:18px;color:#CBD5E1;">
AI-Powered Resume Evaluation & Skill Gap Discovery
</p>

<br>

<div style="
display:flex;
justify-content:center;
gap:35px;
flex-wrap:wrap;
font-size:17px;">

<div>📊 Resume Dashboard</div>

<div>🤖 AI Analysis</div>

<div>📄 PDF Report</div>

<div>📈 Skill Analytics</div>

<div>🎯 Match Score</div>

<div>💡 Recommendations</div>

</div>

<br>

<hr style="border:1px solid #334155;">

<h4 style="color:#38BDF8;">
Powered by
</h4>

<p style="font-size:17px;">
🐍 Python &nbsp;&nbsp;|&nbsp;&nbsp;
⚡ Streamlit &nbsp;&nbsp;|&nbsp;&nbsp;
🤖 Gemini AI &nbsp;&nbsp;|&nbsp;&nbsp;
📊 Plotly &nbsp;&nbsp;|&nbsp;&nbsp;
📄 ReportLab
</p>

<br>

<p style="font-size:15px;color:#CBD5E1;">

Developed with ❤️ by <b>Mehak</b>

</p>

<p style="font-size:13px;color:#94A3B8;">
© 2026 Resume Intelligence Platform
</p>

</div>

""", unsafe_allow_html=True)

