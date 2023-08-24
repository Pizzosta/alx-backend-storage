#!/usr/bin/env python3
""" Stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(logs_collection, option=None):
    """
    Get statistics about Nginx logs stored in MongoDB.

    Args:
        logs_collection: The MongoDB collection containing the logs.
        option: An HTTP method to filter the logs by. Defaults to None
    Returns:
        None
    """
    #total_logs (int): The total number of logs in the collection.
    total_logs = logs_collection.count_documents({})
    print("{} logs".format(total_logs))

    if option:
        if option in METHODS:
        #method_counts (dict): A dictionary containing counts of each HTTP method used.
            method_count = logs_collection.count_documents({"method": option})
            print("method {}: {}".format(option, method_count))
        return

    for method in methods:
        method_count = logs_collection.count_documents({"method": method})
        print("method {}: {}".format(method, method_count))

    #status_check_count (int): The count of logs with method GET and path /status.
    status_check_count = logs_collection.count_documents(
            {"method": "GET", "path": "/status"})
    print("{} status check".format(status_check_count))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
