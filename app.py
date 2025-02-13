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
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({"error": "Try again"}), 400

    user_input = data['text']
    extracted_name = extract_name(user_input)
    extracted_department, extracted_year = extract_department_year(user_input)

    students = get_students_by_name(extracted_name) if extracted_name else []
    
    if not students and not extracted_department and not extracted_year:
        return jsonify({"error": "No relevant data found"}), 404

    return jsonify({
        "students": students,
        "extracted_department": extracted_department,
        "extracted_year": extracted_year
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
