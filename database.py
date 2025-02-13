from pymongo import MongoClient
import re

# Connect to MongoDB
client = MongoClient("mongodb+srv://MongoVoiceAssistant1:MongoVoiceAssistant1@clusterdbvoicebot.vfdos.mongodb.net/?retryWrites=true&w=majority&appName=ClusterDbVoicebot")
db = client["College_department"]
collection = db["AIDS"]

def get_students_by_name(student_name):
    """
    Search for students using case-insensitive substring matching across multiple years.
    """
    student_name = student_name.strip()
    year_fields = ["SECONDYEAR", "THIRDYEAR", "FOURTHYEAR"]
    matched_students = []

    for year_field in year_fields:
        sample_doc = collection.find_one({year_field: {"$exists": True}})
        if sample_doc and year_field in sample_doc:
            student_records = sample_doc[year_field]
            for student in student_records:
                if "NAME" in student and re.search(student_name, student["NAME"], re.IGNORECASE):
                    matched_students.append({
                        "name": student["NAME"],
                        "year": year_field,
                        "block": student.get("BLOCK", "Unknown"),
                        "room": student.get("ROOM", "Unknown")
                    })

    return matched_students if matched_students else None

