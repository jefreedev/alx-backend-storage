#!/usr/bin/env python3
"""
Module: Where can I learn Python?
"""
def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic.
    """
    tmp = mongo_collection.find({"topics": topic})
    return tmp
