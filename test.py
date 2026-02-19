import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
print(client.list_database_names())
db = client['h2_computing']
print(db.list_collection_names())
coll = db['students']
cursor = coll.find({}, {'_id': 0})
for doc in cursor:
    print(doc)