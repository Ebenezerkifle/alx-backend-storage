#!/usr/bin/env python3
"""A python script to fetch all list of documents"""
import pymongo

def list_all(mongo_collection):
    """ lists all documents in a given collection"""
    print(mongo_collection)
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
