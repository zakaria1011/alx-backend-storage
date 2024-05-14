#!/usr/bin/env python3
""" operations with pymongo"""


def update_topics(mongo_collection, name, topics):
    """ upadate topic in documents"""
    filter_query = {"name": name}
    update_query = {"$set": {"topics": topics}}
    return mongo_collection.update_one(filter_query, update_query)
