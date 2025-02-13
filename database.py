from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://MongoVoiceAssistant1:MongoVoiceAssistant1@clusterdbvoicebot.vfdos.mongodb.net/?retryWrites=true&w=majority&appName=ClusterDbVoicebot")
db = client["College_department"]
collection = db["AIDS"]

# Define department and year keywords
DEPARTMENTS = ["AI&DS", "CSE", "ECE", "IT", "MECH", "CIVIL", "EEE"]  
YEARS = ["first year", "second year", "third year", "fourth year"]

def extract_department_year(text):
    """
    Extract department and year from user input.
    """
    text = text.lower()

    # Find department
    extracted_department = None
    for dept in DEPARTMENTS:
        if dept.lower() in text:
            extracted_department = dept
            break

    # Find year
    extracted_year = None
    for year in YEARS:
        if year in text:
            extracted_year = year.split()[0]  # Extract only "first", "second", etc.
            break

    return extracted_department, extracted_year

def get_students_by_name(student_name):
    """
    Search for students using case-insensitive substring matching across multiple years.
    """
    student_name = student_name.strip().lower()
    year_fields = ["SECONDYEAR", "THIRDYEAR", "FOURTHYEAR"]
    
    matched_students = []
    
    for year_field in year_fields:
        sample_doc = collection.find_one({year_field: {"$exists": True}})  
        if sample_doc and year_field in sample_doc:
            student_records = sample_doc[year_field]
            
            for student in student_records:
                if "NAME" in student and student_name in student["NAME"].strip().lower():
                    matched_students.append({
                        "student": student,  
                        "year": year_field
                    })
    
    return matched_students
