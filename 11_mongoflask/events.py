#Peihua Huang, Jackie Lin (Team Concrastinators)
#SoftDev1 pd1
#K11 -- Import/Export Bank
#2020-03-04

'''The dataset we used is called the Historical Events API from Vizgr. It contains a list of events in history (in English), with each result
containing a date, a description, a category. Each event is categorized either by location or by topic. Within these broad categories, each event may
also fall under subcategories. For example, an event categorized by location may fall under the subcategory 'Egypt'. The raw data is hosted at
http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=en. The dataset was imported into the database
through a series of steps. Since all the events were contained within a key-value pair called 'results', the file was first spliced to return only the
string of the list of events (for easier parsing). Since the dataset was not separated by newlines but each entry started with the word 'events', the dataset was split
using the word 'events'. Then, one by one, the items in this list were formatted (removed extra commas) and json.loads() was used to turn it into a dictionary
that was then inserted into the Mongo database.'''

import json
from pymongo import MongoClient

client = MongoClient()
db = client.croissants
events = db.events

def create_events():
    events.drop()
    with open('dataset.json') as file:
        data = file.read() #convert file to str
        data = data[30:-3] #clean up file
        data = data.split("\"event\": ") #list of events
        data.pop(0) #empty entry
        for item in data:
            if item[-1] == ' ':
                item = item[0:-2] #formatting JSON object
            item = json.loads(item) #load object
            events.insert_one(item) #insert into database

def get_by_place(location):
    '''Returns all events that happened in a certain region'''
    results = events.find({"category2" : location})
    return results

def get_by_year(year):
    '''Returns all events that happened in a certain year'''
    results = events.find({ "date": {'$regex' : str(year)} })
    return results

def get_by_topic(topic):
    '''Returns all events that fall under a certain topic'''
    regex = "(\w*%s\w*)" % topic
    query = {"category2":{"$regex": regex, "$options": "i"}}
    results = events.find(query)
    return results

def get_by_keyword(keyword):
    '''Returns all events with given keyword in their description'''
    regex = "(\w*%s\w*)" % keyword
    query = {"description":{"$regex": regex, "$options": "i"}}
    results = events.find(query)
    return results
