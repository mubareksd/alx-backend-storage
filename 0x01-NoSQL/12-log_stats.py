#!/usr/bin/env python3
"""12-log_stats module
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    collection = db.nginx
    count = collection.count_documents({})
    status_check_count = collection.count_documents({"path": "/status"})
    print(f"{count} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {count}")
    print(f"{status_check_count} status check")
