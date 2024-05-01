#!/usr/bin/env python3
"""
Providing some stats about Nginx logs
"""
from pymongo import MongoClient


def print_logs_nginx_requests(collection):
    """
    Prints the number of logs stored in logs
    """
    print(f"{collection.estimated_document_count()} logs")
    print("Methods:")
    print(f"\tmethod GET: {collection.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {collection.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {collection.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {collection.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {collection.count_documents({'method': 'DELETE'})}")

    print(f"{len(list(collection.find({'method': 'GET', 'path': '/status'})))} status check")

    print("IPs:")
    ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")


def main():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    print_logs_nginx_requests(logs)


if __name__ == "__main__":
    main()
