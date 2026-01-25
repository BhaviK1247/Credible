from utils.evidence import retrieve_evidence

claim = "NASA discovered water on Mars"

evidence = retrieve_evidence(claim)

print("CLAIM:")
print(claim)

print("\nEVIDENCE:")
print(evidence)
