from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_students_by_name
from nlp_processing import extract_name, extract_department_year
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests (Frontend on Vercel)

# ✅ Root Route for Testing (Fixes 404 Not Found)
@app.route("/")
def home():
    return jsonify({"message": "Backend is running successfully!"}), 200

@app.route("/process_voice", methods=["POST"])
def process_voice():
    print("Headers:", request.headers)  # Debugging: Print headers
    print("Raw Data:", request.data)  # Debugging: Print raw request body
    print("JSON Data:", request.get_json())  # Debugging: Check parsed JSON
    
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data found"}), 400  # 400 Bad Request
    
    return jsonify({"message": "Received!", "data": data})


@app.route('/filter_students', methods=['POST'])
def filter_students():
    data = request.json
    user_input = data.get('text', '')
    
    # Extract department and year
    extracted_department, extracted_year = extract_department_year(user_input)

    if not extracted_department or not extracted_year:
        return jsonify({"error": "Try again"}), 400  # Handle incomplete input

    return jsonify({"department": extracted_department, "year": extracted_year})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  # Use PORT from environment or default to 10000
    app.run(host="0.0.0.0", port=port, debug=False)  # ✅ Disable Debug Mode in Deployment
