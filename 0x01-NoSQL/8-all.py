#!/usr/bin/env python3
""" operation with pymongo"""


def list_all(mongo_collection):
    """List all documents in the collection"""
    if mongo_collection.count_documents({}) == 0:
        return []
    return mongo_collection.find()
