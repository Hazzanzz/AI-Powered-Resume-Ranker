"""
This is a Testing for the similarities
"""
from resume_matcher import calculate_similarity

resume = """Experienced Python developer with NLP and data science skills."""
job_desc = """Looking for a data scientist skilled in Python, NLP, and ML models."""

score = calculate_similarity(resume, job_desc)
print("Similarity Score:", score)
