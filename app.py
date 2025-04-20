"""
In this we going to be running StreamLit UI because it allows us to build applications 
with these kind of minimal programming with ease, also it is very accessibile when interacting with
data through intutive interfaces, which enables better decision making 
"""

from dotenv import load_dotenv 
import streamlit as st
from PyPDF2 import PdfReader
from chatgpt_improver import suggest_resume_improvements
from resume_matcher import calculate_similarity
from keyword_extractor import extract_keywords



def read_pdf(file):  # This is for the PDF reader
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


st.set_page_config(page_title="AI Resume Ranker", layout="centered") # This is for our StreamLit UI Application set-up

st.title(" AI-Powered Resume Ranker")
st.markdown("Upload your resume and a job description to check your fit score and get keyword analysis.")

# This is where the user uploads their resume (PDF)
resume_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])
job_desc_file = st.file_uploader("Upload Job Description (TXT)", type=["txt"])

# This is where all the majic begins and where we will start the extraction and modelling process
if resume_file and job_desc_file:
    if st.button("💡 Analyze Resume"):
        with st.spinner("Extracting and analyzing..."):
            # Here is where it would start reading the inputs
            resume_text = read_pdf(resume_file)
            job_description = job_desc_file.read().decode("utf-8")

            # Semantic similarity
            similarity = calculate_similarity(resume_text, job_description)

            # The keyword extracting or searcher
            resume_keywords = extract_keywords(resume_text)
            job_keywords = extract_keywords(job_description)

        # Output results
        st.success(f" **Match Score:** {similarity * 100:.2f}%")
        st.subheader(" Top Resume Keywords")
        st.write(resume_keywords)

        st.subheader("📄 Top Job Description Keywords")
        st.write(job_keywords)
