#!/usr/bin/env python3
"""
Module: Top students
"""
def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    return mongo_collection.aggregate([
        {"$project": {
            "name:" "$name",
            "average_score:" {"$avg:" "$topics.score"}
        }},
        {"$sort": {"average_score": -1}}
    ])
