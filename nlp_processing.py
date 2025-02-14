import re

def extract_name(text):
    name_pattern = r"\b[A-Z]?[a-z]+\s?[A-Z]?[a-z]*\b"  # Allow names starting with lowercase
    matches = re.findall(name_pattern, text, re.IGNORECASE)  # Case-insensitive search
    return matches[0] if matches else None


def extract_department_year(text):
    department_keywords = {
        "artificial intelligence and data science": "AI&DS",
        "aids": "AI&DS",
        "computer science": "CSE",
        "cs": "CSE",
        "electronics and communication": "ECE",
        "ece": "ECE"
    }
    
    year_keywords = {
        "first year": "I",
        "second year": "II",
        "third year": "III",
        "fourth year": "IV",
        "1st year": "I",
        "2nd year": "II",
        "3rd year": "III",
        "4th year": "IV"
    }
    
    extracted_department = None
    extracted_year = None

    for key, value in department_keywords.items():
        if key in text.lower():
            extracted_department = value
            break

    for key, value in year_keywords.items():
        if key in text.lower():
            extracted_year = value
            break

    return extracted_department, extracted_year
