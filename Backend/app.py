from flask import Flask, request, jsonify
from flask_cors import CORS
import fact_checker

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    print("Received:", data)  

    text = data.get("news", "")  

    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = fact_checker.run_fact_checker(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)