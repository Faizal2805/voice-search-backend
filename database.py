from pymongo import MongoClient
import os

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI")  # Ensure you have set this in Render
client = MongoClient(MONGO_URI)
db = client["College_department"]

def get_students_by_name(name):
    """Retrieve students from MongoDB based on a flexible name match."""
    collection_list = ["SECONDYEAR", "THIRDYEAR", "FOURTHYEAR"]  # Modify as needed
    students = []

    # Search in each collection
    for collection_name in collection_list:
        collection = db["AIDS"][collection_name]  # Adjust department structure if needed

        # 🔥 Perform a **case-insensitive, partial match** instead of exact match
        query = {"name": {"$regex": f"^{name}", "$options": "i"}}  # Matches "Hari", "Hari Narayan", etc.
        results = list(collection.find(query, {"_id": 0}))  # Exclude MongoDB Object ID

        if results:
            students.extend(results)

    return students  # Returns a list of student records
