#!/usr/bin/env python3
"""12-log_stats module
"""
from pymongo import MongoClient


def run():
    """run function"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx = client.logs.nginx
    logs = nginx.count_documents({})
    print("{} logs".format(logs))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx.count_documents({"method": method})
        print("\tmethod {}".format(count))
    stats = nginx.count_documents({"path": "/status"})
    print("{} status check".format(stats))


if __name__ == "__main__":
    run()
