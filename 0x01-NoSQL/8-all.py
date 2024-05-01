#!/usr/bin/env python3
"""List all mongo documents in Python
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    """
    return [dc for dc in mongo_collection.find()]
