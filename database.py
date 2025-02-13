import pymongo
from config import MONGO_URI, DATABASE_NAME, COLLECTIONS

client = pymongo.MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

def get_students_by_name(name):
    results = []
    for collection_name in COLLECTIONS:
        collection = db[collection_name]
        students = collection.find({"NAME": {"$regex": f"^{name}", "$options": "i"}})
        results.extend(students)
    
    return [{key: value for key, value in student.items() if key != '_id'} for student in results]
