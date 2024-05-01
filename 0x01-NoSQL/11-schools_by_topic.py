#!/usr/bin/env python3
"""
Returning a list of school
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return a list of schools having a specific topic
    """
    return mongo_collection.find({"topics": topic})
