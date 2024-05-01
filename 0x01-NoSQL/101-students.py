#!/usr/bin/env python3
"""
A function returning all students:
"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns all students sorted by their average score
    """
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
