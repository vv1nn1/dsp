"""
Q1. Find how many different degrees there are, and their frequencies: Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
"""
import csv
import re
def count_degrees(csv_file_name):
    with open(csv_file_name, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    data.pop(0)
    #degrees = [x[1].replace('.','').upper().split() for x in data]    
    
    #[^\w\s] match anything that's not alphanumeric or underscore and not space
    degrees = [re.sub(r'[^\w\s]', '', x[1]).split() for x in data]
    count = {}
    for i in degrees:    
        for j in i:
            if j in count: count[j] += 1
            else: count[j] = 1
    return count

  
"""
Q2. Find how many different titles there are, and their frequencies: Ex: Assistant Professor, Professor
"""
  
import csv
def count_titles(csv_file_name):
    
    with open(csv_file_name, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    data.pop(0)
    titles = [x[2].lower()[:9] for x in data]
    count={}
    for i in titles:
        if i not in count:
            count[i] = 1
        else:
            count[i] +=1
    return count

"""
Q3. Search for email addresses and put them in a list. Print the list of email addresses.
"""
import csv
import re

def emails(csv_file_name):
    
    with open(csv_file_name, 'r') as f:
        data = f.read().lower()
        #data = [row for row in csv.reader(f.read().splitlines())]
    #data.pop(0)
    #regex = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
    #                "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
    #                "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))
    
    match = [email for email in re.findall(r'[\w\.-]+@[\w\.-]+', data)]
    return match
  
"""
Q4. Find how many different email domains there are (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). 
Print the list of unique email domains.
"""
import re

def unique_domains(emails):
    
    #\w+ matches any word character (equal to [a-zA-Z0-9_])
    #+ Quantifier — Matches between one and unlimited times, as many times as possible, giving back as needed 
    email = [re.search(r'@(\w+.+)', i).group(1) for i in emails]
    return set(email)
