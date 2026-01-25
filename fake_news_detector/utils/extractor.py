from newspaper import Article
import re

def extract_article_text(input_data: str) -> str:
   
    if input_data.startswith("http"):
        try:
            article = Article(input_data)
            article.download()
            article.parse()
            return article.text
        except Exception as e:
            print(f"Error downloading or parsing URL: {e}")
            return ""  # return empty string if failed
    else:
        return input_data

def clean_text(text: str) -> str:
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text).strip()
