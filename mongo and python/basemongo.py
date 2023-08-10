from pymongo import MongoClient


class BaseMongo:
    def __init__(self, db_name, collection_name):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def insert_many(self, documents):
        return self.collection.insert_many(documents)

    def find_one(self, query):
        return self.collection.find_one(query)

    def find(self, query):
        return list(self.collection.find(query))
