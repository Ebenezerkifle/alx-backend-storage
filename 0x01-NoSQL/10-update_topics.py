#!/usr/bin/env python3
"""A python script that changes all topics of a school
document based on the name"""
import pymongo

def update_topics(mongo_collection, name, topics):
    mongo_collection.update_many({"name": name}, {"$set" : {
        "topics": topics
    }})
