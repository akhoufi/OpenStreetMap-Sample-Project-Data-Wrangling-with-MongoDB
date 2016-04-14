# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 22:47:02 2016

@author: akhou
"""
import json

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client.p3
print db.tunisia.find().count() 
print  db.tunisia.find({"type":"node"}).count()
print  db.tunisia.find({"type":"way"}).count()
print db.tunisia.distinct({"created.user"}).length
db.tunisia.aggregate([{"$match":{"amenity":{"$exists":1}}}, {"$group":{"_id":"$amenity","count":{"$sum":1}}}, {"$sort":{"count":­1}}, {"$limit":10}])