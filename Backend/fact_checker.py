import google.generativeai as genai
import json
import re

# Configure API
genai.configure(api_key="Paste Your Api key ")

# Load model
model = genai.GenerativeModel("models/gemini-2.5-flash")

def run_fact_checker(news_text):
    prompt = f"""
You are a fact-checking AI.

Analyze the following news and respond ONLY in valid JSON format:

{{
  "verdict": "True | False | Misleading",
  "confidence": number between 0 and 100,
  "explanation": "short explanation"
}}

News:
\"\"\"{news_text}\"\"\"
"""

    response = model.generate_content(
        prompt,
        generation_config={"temperature": 0}
    )

    raw_text = response.text.strip()

    #  Gemini sometimes wraps JSON in markdown — clean it
    raw_text = re.sub(r"```json|```", "", raw_text).strip()

    try:
        result = json.loads(raw_text)
        return result
    except json.JSONDecodeError:
        return {
            "verdict": "Misleading",
            "confidence": 50,
            "explanation": "Unable to parse model response reliably."
        }
