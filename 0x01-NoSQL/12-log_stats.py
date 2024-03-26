#!/usr/bin/env python3
"""12-log_stats"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
log_collection= client.logs.nginx

total_doc = log_collection.count_documents({})
gets = log_collection.count_documents({"method" : "GET"})
posts = log_collection.count_documents({"method" : "POST"})
puts = log_collection.count_documents({"method" : "PUT"})
patches = log_collection.count_documents({"method" : "PATCH"})
deletes = log_collection.count_documents({"method" : "DELETE"})
get_status = log_collection.count_documents({ '$and': [{"method" : "GET"}, {"path" : "/status"}]})

print('''
      {} logs
      Methods:
        method GET: {}
        method POST: {}
        method PUT: {}
        method PATCH: {}
        method DELETE: {}
      {} status check
      '''
      .format(total_doc, gets, posts, puts, patches, deletes, get_status))
