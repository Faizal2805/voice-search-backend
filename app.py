from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_student_details, extract_department_year
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
    Process voice input and return either student details or extracted department/year.
    """
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({"error": "Try again"}), 400

    user_input = data['text']
    
    # Check if input contains a name
    extracted_name = extract_name(user_input)
    if extracted_name:
        student_details = get_student_details(extracted_name)
        if student_details:
            return jsonify({"student_details": student_details})
        return jsonify({"error": "Student not found"}), 404

    # If no name is found, extract department and year
    extracted_department, extracted_year = extract_department_year(user_input)
    
    return jsonify({
        "extracted_department": extracted_department,
        "extracted_year": extracted_year
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
