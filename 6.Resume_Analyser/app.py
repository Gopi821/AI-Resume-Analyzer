import streamlit as st

from utils.pdf_reader import extract_text
from utils.skill_extractor import extract_skills
from utils.matcher import calculate_similarity

st.title(":red[🤖 AI Resume Analyzer] :violet[& Job Match Engine]")


uploaded_resume = st.file_uploader(
    ":blue[📄 Upload Resume PDF]",
    type=["pdf"]
)

job_description = st.text_area(
    ":orange[📝 Paste Job Description Here]"
)

if uploaded_resume and job_description:

    resume_text = extract_text(uploaded_resume)

    score = calculate_similarity(
        resume_text,
        job_description
    )

    resume_skills = extract_skills(
        resume_text
    )

    job_skills = extract_skills(
        job_description
    )

    missing_skills = list(
        set(job_skills) -
        set(resume_skills)
    )

    st.subheader(":rainbow[✅ Match Score]")
    st.success(f"{score}%")

    st.subheader(":blue[🛠 Resume Skills]")
    st.write(resume_skills)

    st.subheader(":violet[📋 Job Skills]")
    st.write(job_skills)

    st.subheader(":red[❌ Missing Skills]")
    st.write(missing_skills)