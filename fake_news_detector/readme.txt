## Folder Structure

```
fake_news_detector/
│
├── main.py                 # Entry point (interactive input)
├── utils/                  # Helper modules
│   ├── extractor.py        # Article extraction & text cleaning
│   ├── claims.py           # Claim extraction
│   ├── evidence.py         # Evidence retrieval from DuckDuckGo
│   └── verifier.py         # Claim verification using LLM
└── requirements.txt        # Required Python packages
```

---

## ✅ Installation

1. **Clone or download the folder** to your local machine.
2. **Create a virtual environment** (optional but recommended):

```bash
python -m venv venv
# Activate venv:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

**Or manually:**

```bash
pip install nltk newspaper3k torch transformers ddgs
```

4. NLTK will automatically download required data (`punkt`) when running the program.

---

## ▶ How to Run

Run the system from CMD:

```bash
python main.py
```

* The program will **prompt you**:

```
Enter the news article URL or raw text:
```

* Enter either:

  * A **news article URL**, e.g.:

    ```
    https://www.bbc.com/news/world-us-canada-66741438
    ```
  * Or **raw news text**, e.g.:

    ```
    NASA confirms discovery of water on Mars.
    ```

* The program will process the input and print a **JSON output** like:

```json
{
    "claims_analyzed": 2,
    "claims": [
        {
            "claim": "NASA confirms discovery of water on Mars.",
            "truth_score": 0.82
        },
        {
            "claim": "This discovery enables future colonization.",
            "truth_score": 0.45
        }
    ],
    "average_truth_score": 0.635,
    "final_verdict": "UNCERTAIN"
}
```


