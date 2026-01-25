from utils.verifier import verify_claim

claim = "NASA discovered water on Mars"

evidence = (
    "NASA confirmed in 2018 that liquid water exists beneath the surface of Mars, "
    "based on radar data collected by the Mars Express spacecraft."
)

result = verify_claim(claim, evidence)

print("CLAIM:", claim)
print("VERDICT:", result["label"])
print("CONFIDENCE:", result["confidence"])
