#!/usr/bin/env python3
""" Log stats - improved version """
from pymongo import MongoClient

HTTP_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]
TOP_IP_LIMIT = 10


def get_top_ips(collection):
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": TOP_IP_LIMIT},
        {"$project": {"_id": 0, "ip": "$_id", "count": 1}}
    ]
    return collection.aggregate(pipeline)


def nginx_stats_check():
    client = MongoClient()
    collection = client.logs.nginx

    num_of_docs = collection.count_documents({})
    print(f"{num_of_docs} logs")

    print("Methods:")
    for method in HTTP_METHODS:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_count = collection.count_documents(
            {"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

    print("IPs:")
    top_ips = get_top_ips(collection)
    for top_ip in top_ips:
        ip_address = top_ip.get("ip")
        count = top_ip.get("count")
        print(f"\t{ip_address}: {count}")


if __name__ == "__main__":
    nginx_stats_check()
