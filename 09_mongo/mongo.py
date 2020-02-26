#Peihua Huang, Jackie Lin
#SoftDev1 pd1
#K09 -- Yummy Mongo Py
#2020-02-26


from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient()
db = client.test
db.restaurants.drop()
restaurants = db.restaurants
file = open("primer-dataset.json", "r")
content = file.readlines()
for line in content:
    restaurants.insert_one(loads(line))
#for item in restaurants.find({}):
#    print(item)

def find_borough(borough):
    '''All restaurants in a specified borough'''
    return restaurants.find({"borough" : borough})

def find_zipcode(zipcode):
    '''All restaurants in a specified zip code'''
    return restaurants.find({"address.zipcode" : zipcode})

def find_zip_grade(zipcode, grade):
    '''All restaurants in a specified zip code and with a specified grade.'''
    return restaurants.find({"address.zipcode" : zipcode, "grades.grade" : grade})

def find_zip_score(zipcode, score):
    '''All restaurants in a specified zip code with a score below a specified threshold.'''
    return restaurants.find({"address.zipcode": zipcode, "grades.score" : {"$lt" : score}})

for rest in find_borough("Brooklyn"):
    print(rest)

for rest in find_zipcode("11225"):
    print(rest)

for rest in find_zip_grade("10462", "A"):
    print(rest)

for rest in find_zip_score("10019", 4):
    print(rest)
