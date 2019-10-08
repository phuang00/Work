#Peihua Huang, Hannah Fried
#SoftDev1 pd2
#K17 -- SQLITE3 BASICS
#2019-10-07

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >
def makeTable(filename):
    with open(filename + ".csv") as file:
    # open csv file
        csv_reader = csv.DictReader(file)
        # create DictReader that maps the values in each row to an OrderedDict
        # with the keys as the first row of the csv file
        headers = list(csv_reader.fieldnames)
        # create a list of the keys/headers
        c.execute("CREATE TABLE {}({} TEXT, {} INTEGER, {} INTEGER)".format(filename, headers[0], headers[1], headers[2]))
        # create a table in the db with the headers as column names
        for row in csv_reader:
        # for each row of values in the reader
            c.execute("INSERT INTO {} VALUES(\"{}\", {}, {})".format(filename, row[headers[0]], row[headers[1]], row[headers[2]]))
            # insert the values into the table

makeTable("courses")
makeTable("students")
# run the function on both csv files

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
