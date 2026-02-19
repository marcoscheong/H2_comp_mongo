#CREATE OPERATION
import pymongo 
from docs import document

#Connect to MongoClient

client = pymongo.MongoClient('127.0.0.1', 27017)

#Selects the Database
db = client['h2_computing']
coll = db['students']

#INSERTION
#multiple dicts in a list so insert_many() BUT if its only 1 dict, insert_one()
result = coll.insert_many(document)

client.close()
