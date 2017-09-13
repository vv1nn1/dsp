"""
Q6.
"""
import csv
from collections import defaultdict
def get_dict():
    with open('faculty.csv','r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    data.pop(0)
    answer = defaultdict(list)
    
    for row in data:    
        lastname = row[0].split(" ")
        #print(lastname)
        #i = 0
        #while (lastname[-1],i) in answer:
        #    i+=1
        #answer[(lastname[-1],i)] = row[1:]
        answer[lastname[-1]].append(row[1:])
		
    return answer

"""
Q7.
"""
import csv

def get_dict():

    with open('faculty.csv','r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    data.pop(0)
    answer = {}
    for row in data:
        name = row[0].split(" ")     
        answer[tuple(name)] = row[1:]
    
    return answer

"""
Q8.
"""
import csv
from collections import OrderedDict

def get_dict():

    with open('faculty.csv','r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    data.pop(0)
    answer = {}
    for row in data:
        name = row[0].split(" ")
        answer[tuple(name)] = row[1:]
        
    answer_new = OrderedDict(sorted(answer.items(),  key=lambda t: t[0][-1]))
    print(dict(list(answer_new.items())[:5]))
    return answer
