#!/usr/bin/env python3
"""12-log_stats module
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx = client.logs.nginx
    logs = nginx.count_documents({})
    print(f"{logs} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    stats = nginx.count_documents({"path": "/status"})
    print(f"{stats} status check")
