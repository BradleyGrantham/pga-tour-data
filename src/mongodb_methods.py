from pymongo import MongoClient


def update_collection(document, database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    coll.update_one(document, {'$set': document}, upsert=True)


def read_field_from_collection(field, database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    for doc in coll.find({}, {field: True}):
        yield doc[field]


def retrieve_document(field, value, database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return coll.find_one({field: value})