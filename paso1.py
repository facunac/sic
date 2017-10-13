#!/usr/bin/env python

import pymongo

client = pymongo.MongoClient("mongodb://dec_user:PJoafIu0M01M5gzI@decdev-shard-00-00-fzh1i.mongodb.net:27017,decdev-shard-00-01-fzh1i.mongodb.net:27017,decdev-shard-00-02-fzh1i.mongodb.net:27017/test?ssl=true&replicaSet=decdev-shard-0&authSource=admin")

db = client.test

col = db.users

col.find_one({"email": "orland@leffler.biz"})

print col.id

