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

    print(count)
    print("Methods:")
    print("    method GET: {}".format(get_count))
    print("    method POST: {}".format(post_count))
    print("    method PUT: {}".format(put_count))
    print("    method PATCH: {}".format(patch_count))
    print("    method DELETE: {}".format(delete_count))
    print("{} status check".format(status_check_count))
    pass
