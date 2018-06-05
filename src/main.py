from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://localhost:27017')

grades = client.tracker.grades

for g in grades.find():
    print(g['grade'])

print(sum([g['grade'] for g in grades.find()])/grades.count())

""" for i in range(3):
    name = input('name: ')
    klass = input('class: ')
    grade = float(input('grade: '))
 
    d = {
        'name': name,
        'klass': klass,
        'grade': grade
        }
    grades.insert_one(d)
 """

