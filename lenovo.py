import random as rand

KREWES = {'orpheus':['Emily', 'Kevin'], 'rex':['William', 'Joseph']}

def function(dict):
    teams = list()
    for a in dict.keys():
        teams.append(a)
    team = teams[rand.randint(0,len(dict) - 1)]
    print(dict[team][rand.randint(0,len(dict[team]) - 1)])

function(KREWES)
