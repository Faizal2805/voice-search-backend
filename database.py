from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://MongoVoiceAssistant1:MongoVoiceAssistant1@clusterdbvoicebot.vfdos.mongodb.net/?retryWrites=true&w=majority&appName=ClusterDbVoicebot")
db = client["College_department"]
collection = db["AIDS"]

def get_students_by_name(student_name):
    """
    Search for students using case-insensitive substring matching across multiple years.
    """
    student_name = student_name.strip().lower()  # Normalize case and remove extra spaces
    year_fields = ["SECONDYEAR", "THIRDYEAR", "FOURTHYEAR"]
    
    matched_students = []
    
    for year_field in year_fields:
        sample_doc = collection.find_one({year_field: {"$exists": True}})  # Check if field exists
        if sample_doc and year_field in sample_doc:
            student_records = sample_doc[year_field]  # Extract list of students
            
            # Perform case-insensitive substring match (prefix, infix, midfix)
            for student in student_records:
                if "NAME" in student and student_name in student["NAME"].strip().lower():
                    matched_students.append(student)  # Store only student data
    
    return matched_students

def extract_department_year(user_input):
    """
    Extract department and year from the user input.
    """
    user_input = user_input.lower()
    departments = {"ai&ds": ["aids", "ai and ds", "artificial intelligence and data science"]}
    years = {"II": ["second year", "2nd year", "ii year"]}
    
    extracted_department, extracted_year = None, None
    
    for dept_key, dept_values in departments.items():
        for alias in dept_values:
            if alias in user_input:
                extracted_department = dept_key.upper()
                break
        if extracted_department:
            break
    
    for year_key, year_values in years.items():
        for alias in year_values:
            if alias in user_input:
                extracted_year = year_key
                break
        if extracted_year:
            break
    
    return extracted_department, extracted_year
