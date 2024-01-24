#!/usr/bin/env python3
"""A python function returns the list of school on a topic"""

def schools_by_topic(mongo_collection, topic):
    """returning a list of documents with a specific topic"""
    return list(mongo_collection.find({"topics": topic}))
