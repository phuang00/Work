import random as rand
##import random library

# open the file and read the file by line
fh = open('occupations.csv', 'r')
data = fh.readlines();
fh.close()
data = data[1: len(data) -1]
# remove the first and last line of the file, because they're useless
dict = dict()
for a in data:
    # for every line in the file, remove the white spaces at the end
    a.strip();
    # split the job class and percentage based on whether the job class is in quotes or not
    if (a[0] == '\"'):
        list = a[1:].split('\",')
    else:
        list = a.split(',')
    # add the job class and percentage into dictionary
    dict[list[0]] = float(list[1])

def choose(d):
    choices = []
    # for every job class, percentage pair in the dictionary,
    #   add the job class (percentage * 10) times to the list, since each float has at most 1 place after decimal point
    # (this will weigh the jobs based on their percentage)
    for key,value in d.items():
        # credit: geeksforgeeks website on iterating over a dictionary in Python
        choices += [key] * int(value * 10)
        ## credit: This method of adding to the list (and not using another for loop) was suggest to me by Grace Mao.
    # return a randomly chosen job from the weighted list
    return rand.choice(choices)

print(choose(dict))
