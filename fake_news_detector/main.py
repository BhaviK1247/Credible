import nltk
nltk.download("punkt", quiet=True)
from newspaper import Article
from utils.extractor import clean_text, extract_article_text
from utils.claims import extract_claims
from utils.evidence import retrieve_evidence
from utils.verifier import verify_claim_ensemble

def generate_final_verdict(avg_score: float) -> str:
    if avg_score >= 0.5:
        return "Likely TRUE"
    elif avg_score <= 0.3:
        return "Likely FAKE"
    else:
        return "UNCERTAIN"

def run_fact_checker(input_data: str, max_snippets: int = 15) -> dict:
    # Extract article text
    article_text = extract_article_text(input_data)
    if not article_text:
        return {"claims_analyzed": 0, "claims": [], "average_truth_score": None, "final_verdict": "No claims found"}

    cleaned_text = clean_text(article_text)
    claims = extract_claims(cleaned_text)
    if not claims:
        return {"claims_analyzed": 0, "claims": [], "average_truth_score": None, "final_verdict": "No claims found"}

    claim_results = []
    claim_scores = []

    for claim in claims:
        # Step 1: Retrieve multiple evidence snippets
        evidence_text = retrieve_evidence(claim, max_results=max_snippets)
        evidence_snippets = evidence_text.split("...")

        snippet_scores = []

        # Step 2: Evaluate each snippet with ensemble
        for snippet in evidence_snippets:
            snippet = snippet.strip()
            if not snippet:
                continue
            result = verify_claim_ensemble(claim, snippet)
            snippet_scores.append(result["confidence"])

        # Step 3: Weighted average of top 4 snippets
        snippet_scores.sort(reverse=True)
        top_scores = snippet_scores[:4] if snippet_scores else [0.5]

        # Weighted averaging: weights 0.4, 0.3, 0.2, 0.1
        weights = [0.4, 0.3, 0.2, 0.1]
        weighted_score = sum(s * w for s, w in zip(top_scores, weights[:len(top_scores)])) / sum(weights[:len(top_scores)])

        claim_scores.append(weighted_score)
        claim_results.append({"claim": claim, "truth_score": round(weighted_score, 3)})

    # Step 4: Average across all claims
    avg_score = sum(claim_scores) / len(claim_scores)
    final_verdict = generate_final_verdict(avg_score)

    return {
        "claims_analyzed": len(claims),
        "claims": claim_results,
        "average_truth_score": round(avg_score, 3),
        "final_verdict": final_verdict
    }

if __name__ == "__main__":
    input_data = input("Enter the news article URL or raw text: ").strip()
    if not input_data:
        print("No input provided. Exiting.")
        exit()

    result = run_fact_checker(input_data)

    import json
    print(json.dumps(result, indent=4))
