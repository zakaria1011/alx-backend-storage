#!/usr/bin/env python3
""" operation with  paymongo"""


def insert_school(mongo_collection, **kwargs):
    """ insert a documents"""
    new_school = kwargs
    result = mongo_collection.insert_one(new_school)
    return result.inserted_id
