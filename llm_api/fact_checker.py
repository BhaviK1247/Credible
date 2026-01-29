import google.generativeai as genai

# Configure API
genai.configure(api_key="")

# Load model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Ask input from user
news_text = input("Enter news text or claim to verify:\n> ")

prompt = f"""
You are a fact-checking AI.

Analyze the following news and respond in JSON format:

{{
  "verdict": "True/False/Misleading",
  "confidence": "0-100",
  "explanation": "short explanation"
}}

News:
\"\"\"{news_text}\"\"\"
"""

response = model.generate_content(
    prompt,
    generation_config={"temperature": 0}
)

print("\n--- FACT CHECK RESULT ---")
print(response.text)
