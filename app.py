from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_students_by_name, extract_department_year
from nlp_processing import extract_name
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Voice Search Backend is Running!"})

@app.route('/process_voice', methods=['POST'])
def process_voice():
    """
    Extract the name from text and retrieve student details from the database.
    """
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({"error": "Try again"}), 400

    user_input = data['text']
    extracted_name = extract_name(user_input)  

    if not extracted_name:
        return jsonify({"error": "No name found"}), 404

    students = get_students_by_name(extracted_name)

    return jsonify({"students": students})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
