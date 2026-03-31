from flask import Flask, request, jsonify
from flask_cors import CORS
import fact_checker
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#aniruddha2006",
    database="credible_db"
)

cursor = db.cursor()

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    print("Received:", data)

    text = data.get("news", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = fact_checker.run_fact_checker(text)
    return jsonify(result)


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    try:
        query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        values = (name, email, password)

        cursor.execute(query, values)
        db.commit()

        return jsonify({"message": "Signup successful"})

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    query = "SELECT * FROM users WHERE email=%s AND password=%s"
    cursor.execute(query, (email, password))

    user = cursor.fetchone()

    if user:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"error": "Invalid credentials"})

if __name__ == "__main__":
    app.run(debug=True)