#Task
import pymongo

client = pymongo.MongoClient('127.0.0.1', 27017)
# print(client.list_database_names())
db = client['h2_computing']
# print(db.list_collection_names())
coll = db['students']

# print(coll.find_one({'student_id': 6}, {'_id': 0 }))

# coll.update_one({'student_id': 6}, {'$set':{'tshirt_size': 'S'}})

# coll.delete_many({})

# cursor = coll.find({})
# for data in cursor:
#     print(data)
coll.update_one({'student_id': 8}, {'$set':{'graduated': True}})

# #Advanced Filters


# To retrieve a list of students from the student collection that have the field graduated:

# cursor = coll.find({'graduated': True})


# for doc in cursor:
#     print(doc)

##ELEMENT OPERATORS
cursor = coll.find({'graduated': {'$exist': True}})
cursor = coll.find({'graduated': {'$type': 'bool'}})


##COMPARISON OPERATORS
#To retrieve students with year_enrolled after 2023:
cursor = coll.find({'year_enrolled': {'$gte': 2023}})

# for doc in cursor:
#     print(doc)


##MATCH OPERATORS
#To retrieve all JC1s (enrolled in 2024) and JC2s (enrolled in 2023) from the student collection:
cursor = coll.find({'year_enrolled': {'$in': [2023, 2024]}})

# for doc in cursor:
#     print(doc)

#PROJECTION OPERATORS
#To retrieve all students from AVA in the student collection, where the cca field is an array:
cursor = coll.find({'cca': {'$elemMatch': {'name': 'AVA'}}})

##LOGICAL OPERATORS

#To retrieve a list of students from class 2440 with tshirt_size = 'M' from the student collection:
cursor = coll.find(
    {
        '$and': [
            {'tshirt_size': 'M'},
            {'class_id': 2440}
        ]
    }
)

#To retrieve a list of students from class 2440 with AVA as a CCA from the student collection:
cursor = coll.find(
    {
        '$and': [
            {'cca': {'$in': 'AVA'}},
            {'class_id': 2440}
        ]
    }
)

#Note: This should not be used to match multiple possible values from a single field:


#To query documents that are inside another document, specify the subfield after the field, separated by a period (.).
{
    'tutor_id': 'V Surya',
    'ext_number': 123,
    'pigeonhole': {
        'label': '44',
        'level': 3,
        'row': 4,
        'column': 15
    }
} 

#We can query the list of tutors with pigeon holes outside the staffroom, on level 3
cursor = coll.find({'pigeonhole.level': 3})

#To query the list of tutors whose pigeonholes are at level 3, on the fourth row:
cursor = coll.find(
    {
        '$and': [
            {'pigeonhole.level': 3},
            {'pigeonhole.row': 4},
        ]
    }
)


