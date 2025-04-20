"""
Testing for the Keyword extraction
"""

from keyword_extractor import extract_keywords

sample_text = """
Looking for a software engineer with experience in Python, machine learning, 
NLP, and API development. Experience with Streamlit is a bonus.
"""

keywords = extract_keywords(sample_text)
print("Extracted Keywords:", keywords)
