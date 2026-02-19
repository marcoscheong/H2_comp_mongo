import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['h2_computing']
coll = db['students']

#DELETE ONE
result = coll.delete_one({'student_id':40})

#DELETE MANY 
result = coll.delete_many({})
#displays the amount of documents deleted
print(result.deleted_count)

cursor = coll.find({}, {'_id': 0})
for doc in cursor:
    print(doc)

#DELETING DATABASE (CONVENTIONAL SYNTAX DIFFERENT TO PREVENT MISTAKES)
client.drop_database('h2computing')
#DELETING COLLECTIONS
db.students.drop()