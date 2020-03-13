#Peihua Huang, Henry Liu (Team Computers)
#SoftDev1 pd1
#K10 -- Import/Export Bank
#2020-02-28

# Name of Dataset: Current US Senators
# Description: The dataset contains basic information on all the current US Senators
# Hyperlink: https://www.govtrack.us/api/v2/role?current=true&role_type=senator
# Brief Summary: We imported the dataset by first opening the file and then using loads from bson.json_util to convert the json file into a dictonary. We then inserted each of the senator entries into the mongodb one line at a time.


from bson.json_util import loads
from pymongo import MongoClient

client = MongoClient()
db = client.computers
senators = db.senators

def create_senators():
    senators.drop()
    file = open("primer-dataset.json", "r")
    content = loads(file.read())["objects"]
    for i in range(len(content)):
        senators.insert_one(content[i])


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

def find_description(lastname):
    '''Returns description of all senators with a given last name'''
    return senators.find({"person.lastname" : lastname}, {"_id" : 0, "person.name" : 1, "description" : 1})

def find_num_gender(gender, number):
    '''Return num number of senators of specified gender'''
    return senators.find({"person.gender" : gender}, {"_id" : 0, "person.name" : 1}).limit(number)

# print("-----FINDING ALL SENATORS IN NY-----")
# for item in find_state("NY"):
#     print(item["person"]["name"])
#
# print("-----FINDING ALL DEMOCRATIC SENATORS-----")
# for item in find_party("Democrat"):
#     print(item["person"]["name"])
#
# print("----FINDING ALL FEMALE SENATORS-----")
# for item in find_gender("female"):
#     print(item["person"]["name"])
#
# print("-----FINDING WEBSITE OF SENATORS WHOSE FIRST NAME IS KEVIN-----")
# for item in find_website("Kevin"):
#     print(item["person"]["name"],":", item["website"])
#
# print("-----FINDING DESCRIPTION OF SENATORS WHOSE LAST NAME IS ALEXANDER-----")
# for item in find_description("Alexander"):
#     print(item["person"]["name"], ":", item["description"])
#
# print("-----FINDING 5 MALE SENATORS-----")
# for item in find_num_gender("male", 5):
#     print(item["person"]["name"])
