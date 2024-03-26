#!/usr/bin/env python3
"""12-log_stats"""
from pymongo import MongoClient


def get_stats(log_collection):
    """get statistics about Nginx logs stored in MongoDB"""
    total_doc = log_collection.count_documents({})
    print('{} logs'.format(total_doc))
    print('Methods:')
    gets = log_collection.count_documents({"method": "GET"})
    posts = log_collection.count_documents({"method": "POST"})
    puts = log_collection.count_documents({"method": "PUT"})
    patches = log_collection.count_documents({"method": "PATCH"})
    deletes = log_collection.count_documents({"method": "DELETE"})
    print('    method GET: {}'.format(gets))
    print('    method POST: {}'.format(posts))
    print('    method PUT: {}'.format(puts))
    print('    method PATCH: {}'.format(patches))
    print('    method DELETE: {}'.format(deletes))
    get_status = log_collection.count_documents(
        {'$and': [{"method": "GET"}, {"path": "/status"}]})
    print('{} status check'.format(get_status))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx
    get_stats(log_collection)
