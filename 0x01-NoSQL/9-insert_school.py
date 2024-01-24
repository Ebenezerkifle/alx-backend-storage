#!/usr/bin/env python3
"""A python function that inserts a new document in a collection"""
import pymongo

def insert_school(mongo_collection, **kwargs):
    """insert new document from kwargs"""
    response = mongo_collection.insert_one(kwargs)
    return response.inserted_id
