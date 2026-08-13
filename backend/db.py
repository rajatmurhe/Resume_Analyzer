from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"

client = MongoClient(MONGO_URI)
db = client["hiring_analyzer"]

analysis_collection = db["analysis_logs"]

