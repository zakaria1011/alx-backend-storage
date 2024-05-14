#!/usr/bin/env python3
""" operation with pymongon"""


def schools_by_topic(mongo_collection, topic):
    """ find colection with a topic"""
    filter_query = {"topic": topic}
    schools = mongo_collection.find(filter_query)
    return list(schools)
