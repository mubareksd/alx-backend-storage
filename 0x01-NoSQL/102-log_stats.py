#!/usr/bin/env python3
"""102-log_stats module
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
    print("IPs:")
    ips = nginx.aggregate(
        [
            {"$group": {"_id": "$ip", "sum": {"$sum": 1}}},
            {"$sort": {"sum": -1}},
            {"$limit": 10},
        ]
    )
    for ip in ips:
        sum = ip["sum"]
        ip = ip["_id"]
        print(f"\t{ip}: {sum}")
