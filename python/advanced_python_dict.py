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
