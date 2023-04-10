#!/usr/bin/env python3
"""11-school_by_topic module
"""


def schools_by_topic(mongo_collection, topic):
    """school_by_topic function

    Args:
        mongo_collection: pymongo collection object
        topic (string): topic tobe searched

    Returns:
        topic
    """
    return mongo_collection.find({"topics": topic})
