#!/usr/bin/env python3
""" Function module.
"""
def list_all(mongo_collection):
    """ Lists all documents in a collection.
    Returns: an empty list is no doc. in coll."""
    tmp = mongo_collection.find()
    return tmp
