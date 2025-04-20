""" In this, we have what we call a "keyword extractor", in which this means
that we would be identifing and extracting these significant words or phases from a 
pdf or text which represents the main points or concepts, these are mainly used
when searching index, oven summarizingcontent, which would be also enchancing
the utuility of text data in the this or other application models...
"""

import yake

def extract_keywords(text: str, max_keywords: int = 10) -> list:
    """
    Extracts important keywords from the input text using YAKE.
    Returns a list of keywords sorted by relevance.
    """
    language = "en"
    max_ngram_size = 3
    deduplication_threshold = 0.9

    custom_kw_extractor = yake.KeywordExtractor(
        lan=language,
        n=max_ngram_size,
        dedupLim=deduplication_threshold,
        top=max_keywords,
        features=None
    )

    keywords_with_scores = custom_kw_extractor.extract_keywords(text)
    return [kw for kw, _ in keywords_with_scores]

