import pymongo
from docs import document

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['h2_computing']
coll = db['students']

#Updates first matching document in a collection
result = coll.update_one({'student_id': 25}, {'$set': {'graduated': True}})

#{'student_id': 25, 'student_name': 'Cameron Lewis', 'tshirt_size': 'M', 'class_id': 2455, 'year_enrolled': 2024, 'graduated': 'FALSE'}
#{'student_id': 25, 'student_name': 'Cameron Lewis', 'tshirt_size': 'M', 'class_id': 2455, 'year_enrolled': 2024, 'graduated': True}

#APPLY updates to ALL documents
result = coll.update_many({'student_id':25}, {'$set': {'graduated': False}})

#how many documents matched your filter
print(result.matched_count)
#how many documents were actually changed
print(result.modified_count)

#Remove an existing field in a document ($unset instead of $set) DONT BE CARELESS WITH THIS
result = coll.update_many({'student_id':25}, {'$unset': {'year_enrolled':2024}})

#Replace (only can replace_one)
result = coll.replace_one({'student_id': 25}, {'student_id': 40, 'student_name': 'Test_name', 'tshirt_size': 'M', 'class_id': 2527, 'graduated': True, 'year_enrolled': 2026})
print(result.matched_count)
print(result.modified_count)

cursor = coll.find({}, {'_id': 0})
for doc in cursor:
    print(doc)