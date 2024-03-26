#!/usr/bin/env python3
"""12-log_stats"""
from pymongo import MongoClient


def get_stats(log_collection):
    """get statistics about Nginx logs stored in MongoDB"""
    print('{} logs'.format(log_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(log_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        log_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))

def run():
    """To run function"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_collection = client.logs.nginx
    get_stats(log_collection)


if __name__ == "__main__":
    run()
