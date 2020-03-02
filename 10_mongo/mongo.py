#Peihua Huang, Henry Liu (Team Computers)
#SoftDev1 pd1
#K10 -- Import/Export Bank
#2020-02-28

# Name of Dataset: Current US Senators
# Description: The dataset contains basic information on all the current US Senators
# Hyperlink: https://www.govtrack.us/api/v2/role?current=true&role_type=senator
# Brief Summary:


from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient()
db = client.computers
db.senators.drop()
senators = db.senators
file = open("primer-dataset.json", "r")
content = loads(file.read())["objects"]
for i in range(len(content)):
    senators.insert_one(content[i])
# for item in senators.find({}, {"person.name" : 1}):
#     print(item)


def find_state(state):
    '''Returns all senators representing the specified state'''
    return senators.find({"state" : state}, {"_id" : 0, "person.name" : 1})

def find_party(party):
    '''Returns all senators in specified party'''
    return senators.find({"party" : party}, {"_id" : 0, "person.name" : 1})

def find_gender(gender):
    '''Returns all senators of specified gender'''
    return senators.find({"person.gender" : gender}, {"_id" : 0, "person.name" : 1})

def find_website(firstname):
    '''Returns website of all senators with a given first name'''
    return senators.find({"person.firstname" : firstname}, {"_id" : 0, "person.name" : 1, "website" : 1})

print("-----FINDING ALL SENATORS IN NY-----")
for item in find_state("NY"):
    print(item["person"])

print("-----FINDING ALL DEMOCRATIC SENATORS-----")
for item in find_party("Democrat"):
    print(item["person"])

print("----FINDING ALL FEMALE SENATORS-----")
for item in find_gender("female"):
    print(item["person"])

print("-----FINDING WEBSITE OF SENATORS WHOSE FIRST NAME IS KEVIN")
for item in find_website("Kevin"):
    print(item["person"])





# def find_borough(borough):
#     '''All restaurants in a specified borough'''
#     return restaurants.find({"borough" : borough})
#
# def find_zipcode(zipcode):
#     '''All restaurants in a specified zip code'''
#     return restaurants.find({"address.zipcode" : zipcode})
#
# def find_zip_grade(zipcode, grade):
#     '''All restaurants in a specified zip code and with a specified grade.'''
#     return restaurants.find({"address.zipcode" : zipcode, "grades.grade" : grade})
#
# def find_zip_score(zipcode, score):
#     '''All restaurants in a specified zip code with a score below a specified threshold.'''
#     return restaurants.find({"address.zipcode": zipcode, "grades.score" : {"$lt" : score}})
#
# def find_num_zip(zipcode, number):
#     '''Returns specified number of restaurants in given zip code.'''
#     return restaurants.find({"address.zipcode": zipcode}).limit(number)
#
# print("------------FINDING ALL RESTAURANTS IN BROOKLYN------------")
# for rest in find_borough("Brooklyn"):
#     for key, value in rest.items():
#         if key == "name":
#             print("{name: %s}" % value)
#     #print(rest)
#
# print("------------FINDING ALL RESTAURANTS IN 11225------------")
# for rest in find_zipcode("11225"):
#     for key, value in rest.items():
#         if key == "name":
#             print("{name: %s}" % value)
#     #print(rest)
#
# print("------------FINDING ALL RESTAURANTS IN 10462 with Grade A------------")
# for rest in find_zip_grade("10462", "A"):
#     for key, value in rest.items():
#         if key == "name":
#             print("{name: %s}" % value)
#     #print(rest)
#
# print("------------FINDING ALL RESTAURANTS IN 10019 with Score < 4------------")
# for rest in find_zip_score("10019", 4):
#     for key, value in rest.items():
#         if key == "name":
#             print("{name: %s}" % value)
#     #print(rest)
#
# print("------------FINDING N RESTAURANTS IN GIVEN ZIPCODE------------")
# zip = input("Please enter a zipcode: ")
# while (not zip.isnumeric() or int(zip) < 7005 or int(zip) > 11697):
#     zip = input("Please enter a valid zipcode: ")
# number = input("Please enter the maximum number of results you want to return: ")
# while (not number.isnumeric() or int(number) <= 0):
#     number = input("Please enter an integer greater than zero: ")
# for rest in find_num_zip(zip, int(number)):
#     for key, value in rest.items():
#         if key == "name":
#             print("{name: %s}" % value)
