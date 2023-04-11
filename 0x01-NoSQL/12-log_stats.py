#!/usr/bin/env python3
"""12-log_stats module
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    collection = db.nginx
    count = collection.count_documents({})
    get_count = collection.count_documents({"method": "GET"})
    post_count = collection.count_documents({"method": "POST"})
    put_count = collection.count_documents({"method": "PUT"})
    patch_count = collection.count_documents({"method": "PATCH"})
    delete_count = collection.count_documents({"method": "DELETE"})
    status_check_count = collection.count_documents({"path": "/status"})

    print(f"{count} logs")
    print("Methods:")
    print(f"    method GET: {get_count}")
    print(f"    method POST: {post_count}")
    print(f"    method PUT: {put_count}")
    print(f"    method PATCH: {patch_count}")
    print(f"    method DELETE: {delete_count}")
    print(f"{status_check_count} status check")
