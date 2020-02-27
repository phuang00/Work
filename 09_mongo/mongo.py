#Peihua Huang, Jackie Lin
#SoftDev1 pd1
#K09 -- Yummy Mongo Py
#2020-02-26


from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient()
db = client.test
restaurants = db.restaurants
if (restaurants.count() == 0):
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

def find_num_zip(zipcode, number):
    '''Returns specified number of restaurants in given zip code.'''
    return restaurants.find({"address.zipcode": zipcode}).limit(number)

print("------------FINDING ALL RESTAURANTS IN BROOKLYN------------")
for rest in find_borough("Brooklyn"):
    for key, value in rest.items():
        if key == "name":
            print("{name: %s}" % value)
    #print(rest)

print("------------FINDING ALL RESTAURANTS IN 11225------------")
for rest in find_zipcode("11225"):
    for key, value in rest.items():
        if key == "name":
            print("{name: %s}" % value)
    #print(rest)

print("------------FINDING ALL RESTAURANTS IN 10462 with Grade A------------")
for rest in find_zip_grade("10462", "A"):
    for key, value in rest.items():
        if key == "name":
            print("{name: %s}" % value)
    #print(rest)

print("------------FINDING ALL RESTAURANTS IN 10019 with Score < 4------------")
for rest in find_zip_score("10019", 4):
    for key, value in rest.items():
        if key == "name":
            print("{name: %s}" % value)
    #print(rest)

print("------------FINDING N RESTAURANTS IN GIVEN ZIPCODE------------")
zip = input("Please enter a zipcode: ")
while (not zip.isnumeric() or int(zip) < 7005 or int(zip) > 11697):
    zip = input("Please enter a valid zipcode: ")
number = input("Please enter the maximum number of results you want to return: ")
while (not number.isnumeric() or int(number) < 0):
    number = input("Please enter a valid number: ")
for rest in find_num_zip(zip, int(number)):
    for key, value in rest.items():
        if key == "name":
            print("{name: %s}" % value)
