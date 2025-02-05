import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔹 Replace this with your actual Hugging Face API URL
HF_API_URL = "https://Faizal07-student-faculty-nlp.hf.space/api/predict/"

@app.route("/query", methods=["POST"])
def query_huggingface():
    data = request.json
    user_input = data.get("text", "")

    response = requests.post(HF_API_URL, json={"text": user_input})

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data from Hugging Face"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
