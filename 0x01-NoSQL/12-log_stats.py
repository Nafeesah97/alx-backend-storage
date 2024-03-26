#!/usr/bin/env python3
"""12-log_stats"""
from pymongo import MongoClient


def get_stats(log_collection):
    """get statistics about Nginx logs stored in MongoDB"""
    total_doc = log_collection.count_documents({})
    gets = log_collection.count_documents({"method": "GET"})
    posts = log_collection.count_documents({"method": "POST"})
    puts = log_collection.count_documents({"method": "PUT"})
    patches = log_collection.count_documents({"method": "PATCH"})
    deletes = log_collection.count_documents({"method": "DELETE"})
    get_status = log_collection.count_documents(
        {'$and': [{"method": "GET"}, {"path": "/status"}]})

    print('''{} logs\nMethods:\n\tmethod GET: {}\n\tmethod POST: {}
    \tmethod PUT:{}\n\tmethod PATCH: {}\n\tmethod DELETE: {}\
            \n{} status check'''.format(
            total_doc, gets, posts, puts, patches, deletes, get_status))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx
    get_stats(log_collection)
