#!/usr/bin/env python3
"""12-log_stats"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
log_collection= client.logs.nginx

total_doc = log_collection.count_documents({})
gets = log_collection.find({"method" : "GET"}).count_documents({})
posts = log_collection.find({"method" : "POST"}).count_documents({})
puts = log_collection.find({"method" : "PUT"}).count_documents({})
patches = log_collection.find({"method" : "PATCH"}).count_documents({})
deletes = log_collection.find({"method" : "DELETE"}).count_documents({})
get_status = log_collection.find({ '$and': [{"method" : "GET"}, {"path" : "/status"}]}).count_documents({})

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
