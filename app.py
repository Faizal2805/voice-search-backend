from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_students_by_name
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

def extract_name(text):
    """
    Extracts the name from user input using regex-based approach.
    """
    text = text.lower()
    match = re.search(r"(?:i am looking for|find|search for|looking for)\s+([a-zA-Z]+(?:\s[a-zA-Z]+)*)", text, re.IGNORECASE)
    return match.group(1) if match else None

@app.route("/search", methods=["POST"])
def search_student():
    data = request.json
    user_input = data.get("text", "").strip()
    
    if not user_input:
        return jsonify({"error": "Empty input received"}), 400
    
    extracted_name = extract_name(user_input)
    if not extracted_name:
        return jsonify({"error": "No valid name found in input"}), 400
    
    matched_students = get_students_by_name(extracted_name)
    if not matched_students:
        return jsonify({"message": "No matching student found"}), 404
    
    return jsonify({"students": matched_students}), 200

if __name__ == "__main__":
    app.run(debug=True)
