import random as rand

KREWES = {'orpheus':['Emily', 'Kevin'], 'rex':['William', 'Joseph']}

def function(dict):
    team = dict.keys()[rand.randint(0,len(dict) - 1)]
    print("team" + team)
    #print(dict[team][rand.randint(0,len(team) - 1)])

function(KREWES)
