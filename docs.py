import csv

document = []
with open('students.csv', 'r') as f:
    # The DictReader class allows each row of CSV data to be
    # accessed as a dict, with headers automatically detected
    for doc in csv.DictReader(f):
        doc['class_id'] = int(doc['class_id'])
        doc['student_id'] = int(doc['student_id'])
        doc['year_enrolled'] = int(doc['year_enrolled'])
        document.append(doc)
        