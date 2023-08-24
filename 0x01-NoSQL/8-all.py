#!/usr/bin/env python3
""" List all documents in Python"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """function that lists all documents in a collection."""
    if mongo_collection is None:
        return []
    documents = list(mongo_collection.find())
    return documents
