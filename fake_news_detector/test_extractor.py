from utils.extractor import is_url, clean_text

print(is_url("https://www.bbc.com/news/articles/c3edwx37pd9o"))
print(is_url("NASA discovered water on Mars"))

dirty_text = "NASA   discovered   water \n\n on Mars."
print(clean_text(dirty_text))
