#!/usr/bin/env python3
"""12-log_stats module
"""
from pymongo import MongoClient


def run():
    """run function"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx
    logs = collection.count_documents({})
    print(f"{logs} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {count}")
    stats = collection.count_documents({"path": "/status"})
    print(f"{stats} status check")


if __name__ == "__main__":
    run()
