#!/usr/bin/env python3
"""chnages all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """update_topics function

    Args:
        mongo_colection: pymongo collection object
        name (string): school name to update
        topics (list[string]): list of topics approached in the school

    Returns:
        list:
    """
    return mongo_collection.update_many(
            {"name": name}, {"$set": {"topics": topics}})
