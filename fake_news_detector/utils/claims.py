import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt", quiet=True)

# Conjunctions or phrases to split further within sentences
SPLIT_KEYWORDS = [" and ", " but ", " which ", " that ", "; "]

def extract_claims(text: str):
    claims = []
    # Step 1: split into sentences
    sentences = sent_tokenize(text)

    for sentence in sentences:
        parts = [sentence]

        # Step 2: further split long sentences
        for keyword in SPLIT_KEYWORDS:
            temp = []
            for part in parts:
                temp.extend(part.split(keyword))
            parts = temp

        # Step 3: clean and filter short parts
        for part in parts:
            part = part.strip()
            if len(part.split()) > 5:  # minimum words to be a claim
                claims.append(part)

    return claims
