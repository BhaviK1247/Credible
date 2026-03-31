from google import genai
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def run_fact_checker(news_text):
    try:
        prompt = f"""
        You are a strict JSON generator.

        Return ONLY valid JSON in this exact format:

        {{
          "verdict": "True or False or Misleading",
          "confidence": number,
          "explanation": "short explanation"
        }}

        Do NOT add any extra text, explanation, or formatting.

        News:
        \"\"\"{news_text}\"\"\"
        """

        response = client.models.generate_content(
            model="gemini-1.5-pro",
            contents=prompt
        )

        raw_text = response.text.strip()

        match = re.search(r"\{.*\}", raw_text, re.DOTALL)
        if match:
            raw_text = match.group(0)

        return json.loads(raw_text)

    except Exception as e:
        print("ERROR:", e)
        return {
            "verdict": "Misleading",
            "confidence": 50,
            "explanation": "AI service temporarily unavailable."
        }
