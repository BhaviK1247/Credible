from ddgs import DDGS
import re
from nltk.corpus import stopwords
import nltk

nltk.download("stopwords", quiet=True)
STOPWORDS = set(stopwords.words("english"))

def retrieve_evidence(claim: str, max_results: int = 15) -> str:
    """
    Retrieve relevant evidence snippets from DuckDuckGo for a given claim.
    Filters for snippet relevance and cleans text.
    """
    results = []

    # Extract meaningful keywords (length > 3 and not stopwords)
    keywords = [w.lower() for w in claim.split() if len(w) > 3 and w.lower() not in STOPWORDS]

    with DDGS() as ddgs:
        try:
            for r in ddgs.text(claim, max_results=max_results):
                snippet = r.get("body", "").strip()
                if not snippet:
                    continue

                # Remove dates, lines, and unwanted characters
                snippet = re.sub(r"\d{1,2} [a-zA-Z]+ ago · ", "", snippet)
                snippet = re.sub(r"(Share Save|Click here|Subscribe|Advertisement)", "", snippet, flags=re.IGNORECASE)
                snippet = re.sub(r"[\n\r\t]", " ", snippet)
                snippet = re.sub(r"\s+", " ", snippet)

                snippet_lower = snippet.lower()
                # Keep snippet only if contains at least 2 keywords
                if sum(1 for k in keywords if k in snippet_lower) >= 2:
                    results.append(snippet)

        except Exception as e:
            print(f"Error retrieving evidence: {e}")

    return " ... ".join(results) if results else ""
