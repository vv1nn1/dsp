# Hint:  use Google to find python function

####a) 937days
date_start = '01-02-2013'  
date_stop = '07-28-2015'

def difference_in_days(date1, date2):
    date2 = datetime.strptime(date2,'%m-%d-%Y') 
    date1 = datetime.strptime(date1,'%m-%d-%Y')
    return (date2.date()-date1.date()).days


####b) 513days 
date_start = '12312013'  
date_stop = '05282015'  

def difference_in_days(date1, date2):
    date2 = datetime.strptime(date2,'%m%d%Y') 
    date1 = datetime.strptime(date1,'%m%d%Y')
    return (date2.date()-date1.date()).days

####c) 7850days 
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

def difference_in_days(date1, date2):
    date2 = datetime.strptime(date2,'%d-%b-%Y') 
    date1 = datetime.strptime(date1,'%d-%b-%Y')
    return (date2.date()-date1.date()).days
