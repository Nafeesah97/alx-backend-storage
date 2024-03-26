#!/usr/bin/env python3
"""101-students"""
from pymongo import DESCENDING


def top_students(mongo_collection):
    """returns all students sorted by average score"""
    pipeline = [
        {"$unwind": "$scores"},
        {"$group": {
            "_id": "$_id",
            "student_id": {"$first": "$_id"},
            "average_score": {"$avg": "$scores.score"}
        }},
        {"$sort": {"average_score": -1}}
    ]
    result = list(mongo_collection.aggregate(pipeline))
    return result
