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

def get_student_details(student_name):
    """
    Retrieve student details by name across multiple years.
    """
    student_name = student_name.strip().lower()
    year_fields = ["SECONDYEAR", "THIRDYEAR", "FOURTHYEAR"]
    
    for year_field in year_fields:
        sample_doc = collection.find_one({year_field: {"$exists": True}})
        if sample_doc and year_field in sample_doc:
            student_records = sample_doc[year_field]
            
            for student in student_records:
                if "NAME" in student and student_name in student["NAME"].strip().lower():
                    # Return only relevant student details
                    return {
                        "name": student.get("NAME"),
                        "admission_no": student.get("ADMISSION NO"),
                        "reg_no": student.get("REG NO"),
                        "year": student.get("YEAR"),
                        "department": student.get("DEPARTMENT"),
                        "section": student.get("SECTION"),
                        "room_no": student.get("ROOM NO"),
                        "block": student.get("BLOCK"),
                        "floor": student.get("FLOOR"),
                        "hod_name": student.get("HOD NAME"),
                        "hod_ph": student.get("HOD PH"),
                        "ci_name": student.get("CI NAME"),
                        "ci_ph": student.get("CI PH"),
                    }
    return None
