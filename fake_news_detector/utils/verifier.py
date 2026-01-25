from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

import torch

# Load first model
device = 0 if torch.cuda.is_available() else -1

nli_model_1 = pipeline(
    "zero-shot-classification",
    model="valhalla/distilbart-mnli-12-3",
    device=device
)

# Load second model
nli_model_2 = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli",
    device=device
)

LABELS = ["SUPPORTED", "REFUTED"]

def verify_claim_ensemble(claim: str, evidence: str) -> dict:
    """
    Returns an ensemble confidence score and label for a claim based on evidence.
    """
    # Run both models
    result1 = nli_model_1(evidence, LABELS)
    result2 = nli_model_2(evidence, LABELS)

    # Map labels to confidence
    def get_score(result):
        if "SUPPORTED" in result["labels"]:
            idx = result["labels"].index("SUPPORTED")
            return result["scores"][idx]
        else:
            return 0.5  # fallback

    score1 = get_score(result1)
    score2 = get_score(result2)

    # Ensemble: average of both models
    avg_score = (score1 + score2) / 2

    label = "SUPPORTED" if avg_score >= 0.5 else "REFUTED"

    return {"label": label, "confidence": avg_score}
