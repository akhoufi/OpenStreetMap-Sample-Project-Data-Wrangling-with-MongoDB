# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 22:47:02 2016

@author: akhou
"""
import json

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client.tunisia
with open('tunis_tunisia.osm.json') as f:
    data=[]
    for line in f:
        data .append(json.loads(line))
    db.tunisia.insert(data)
    print db.tunisia.find_one()
