#!/usr/bin/env python3
"""101-students"""
from pymongo import DESCENDING


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": DESCENDING}}
    ]
    return(list(mongo_collection.aggregate(pipeline)))
