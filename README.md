Credible 🛡️

Fact-checking platform to verify news and fight misinformation.

📌 Overview

Credible is an open-source platform designed to help users determine whether news and online information is real, misleading, or fake. It analyzes content using trusted sources, credibility signals, and automated checks to promote accurate and reliable information.


## ⚙️ How to Run the Project


🔹 1. Setup Backend

```bash
cd Backend
pip install -r requirements.txt
🔹 2. Add API Key

Create a .env file inside Backend folder:

GEMINI_API_KEY=your_api_key_here


🔹 3. Run Backend Server
python app.py

Server will run at:
http://127.0.0.1:5000

🔹 4. Run Frontend
Open a new terminal:

cd Frontend
python -m http.server 5500

Open in browser:
http://localhost:5500/index.html


🔐 Authentication
Signup & Login handled using localStorage
Each user has separate history
Can be extended to database integration
