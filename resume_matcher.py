""" This is for a resume Matcher using a Pre-trained model (all-MiniLM-L6-v2)
in which it allows us to be able to have a Very Lightweight and Fast model
that is ready to us to use, we could make a model and train it but for this project
we will be using this given model...
"""
from sentence_transformers import SentenceTransformer, util

# This is to load our Pre-trained model (all-MiniLM-L6-v2)
model = SentenceTransformer('all-MiniLM-L6-v2')  # The model we are using

def calculate_similarity(resume_text: str, job_description: str) -> float:
    """
    Calculates semantic similarity between resume and job description using SBERT.
    Returns a score between 0 and 1.
    """
    # This would encode tecting into vectors
    embeddings = model.encode([resume_text, job_description], convert_to_tensor=True)

    similarity_score = util.pytorch_cos_sim(embeddings[0], embeddings[1]) # cosine similarity

    return round(float(similarity_score), 4)
