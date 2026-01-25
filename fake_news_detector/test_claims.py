import nltk
nltk.download("punkt")

from utils.claims import extract_claims

sample_text = """
NASA discovered water on Mars.
This discovery is important.
In recent years, many believe space exploration is costly.
The findings were published in a scientific journal.
"""

claims = extract_claims(sample_text)

print("Extracted Claims:")
for c in claims:
    print("-", c)
