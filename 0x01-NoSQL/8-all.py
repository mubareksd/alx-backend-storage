#!/usr/bin/env python3
"""8-all module
"""


def list_all(mongo_collection):
    """list_all function

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List: List of Documents
    """
    return mongo_collection.find()
