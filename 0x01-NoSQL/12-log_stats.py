#!/usr/bin/env python3
""" Stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient


def log_stats(logs_collection, option=None):
    """
    Get statistics about Nginx logs stored in MongoDB.

    Returns:
        total_logs (int): The total number of logs in the collection.
        method_counts (dict): A dictionary containing counts of each
        HTTP method used.
            Keys are HTTP methods and values are their corresponding counts.
        status_check_count (int): The count of logs with
        method GET and path /status.
    """
    total_logs = logs_collection.count_documents({})
    print("{} logs".format(total_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    if option:
        if option in METHODS:
            method_count = logs_collection.count_documents({"method": option})
            print("method {}: {}".format(option, method_count))
        return

    for method in methods:
        method_count = logs_collection.count_documents({"method": method})
        print("method {}: {}".format(method, method_count))

    status_check_count = logs_collection.count_documents(
            {"method": "GET", "path": "/status"})
    print("{} status check".format(status_check_count))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
