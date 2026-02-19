import pymongo

client = pymongo.MongoClient("127.0.0.1", 27017)

db = client["h2_computing"]

#collection object from database
coll = db["students"]

#prints a list containg all the DATABASES in the Server
database_list = client.list_database_names()
print(database_list)

#prints a list containing all the COLLECTIONS in the Server
collection_list = db.list_collection_names()
print(collection_list)

#print all documents in a collection
cursor = coll.find({})
for doc in cursor:
    print(doc)

#Test find one document from a collection
print(coll.find_one({'student_id': 6}, {'_id': 0 , "tshirt_size": 1}))

#Test find many document from a collection
cursor = coll.find({'class_id': 2455})
for doc in cursor:
    print(doc)

client.close()