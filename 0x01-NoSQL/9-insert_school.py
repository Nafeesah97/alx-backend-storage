#!/usr/bin/env python3
"""
inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """inserts the arguements into the collection"""
    for items in kwargs:
        mongo_collection.insert({items})
    return mongo_collection.get('_id')