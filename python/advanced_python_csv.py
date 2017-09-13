import csv

def write_to_csv(list_of_emails):
    with open('emails.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter="\n")
        writer.writerow(["list_of_emails"])
        for row in list_of_emails:
            writer.writerow([row])
        #writer.writerow(r for r in list_of_emails)
   
