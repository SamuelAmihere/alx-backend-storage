#!/usr/bin/env python3
"""
Changes all document
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all documents in a collection
    """
    mongo_collection.update_many({"name": name},
                                 {"$set": {"topics": topics}})
