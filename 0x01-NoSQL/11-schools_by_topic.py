#!/usr/bin/env python3
""" Find schools by topic in Python"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of schools having a specific topic."""
    schools = list(mongo_collection.find({"topics": topic}))
    return schools
