#!/usr/bin/env python3
"""101-students"""
from pymongo import DESCENDING


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    pipeline = [
        {
            "$group": {
            "_id": None,
            "averageScore": {"$avg": "topics"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]
    result = list(mongo_collection.aggregate(pipeline))
    return result
