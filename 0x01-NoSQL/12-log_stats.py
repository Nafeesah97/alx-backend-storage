#!/usr/bin/env python3
"""12-log_stats"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
log_collection= client.logs.nginx

total_doc = log_collection.count()
gets = log_collection.find({"method" : "GET"}).count()
posts = log_collection.find({"method" : "POST"}).count()
puts = log_collection.find({"method" : "PUT"}).count()
patches = log_collection.find({"method" : "PATCH"}).count()
deletes = log_collection.find({"method" : "DELETE"}).count()
get_status = log_collection.find({ '$and': [{"method" : "GET"}, {"path" : "/status"}]}).count()

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