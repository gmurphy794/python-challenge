import csv

csvpath = ('/Users/gmurphy794/Documents/GitHub/python-challenge/PyBank/budget_data.csv')
file = open("bankfile.txt", 'w')


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    months = []
    dollarsum = 0
    dollars = []
    change = 0
    chgup = 0 
    chgdwn = 0
    changes = []
    
    for row in csvreader:
        months.append(str(row[0]))
        dollarsum+= int(row[1])
        dollars.append(int(row[1]))
    
    for i in range(1,len(dollars)):
        change = dollars[i] - dollars[i-1]
        changes.append(change)
    
    """for x in changes:"""
        
    del months[0]
    avgchange = sum(changes)/len(changes)
    
    for i in range(len(changes)):
        if changes[i] > chgup:
            chgup = changes[i]
            hmnth = months[i]
        elif changes[i] < chgdwn:
            chgdwn = changes[i]
            lmnth = months[i]
        
    print("Finanancial Analysis")
    print("-----------------------------------------")
    print("Total Months: " + str(len(months) + 1))
    print("Total: $" + str(dollarsum))
    print("Average Change: $" + str(round(avgchange, 2)))
    print("Greatest Increase in Profits:  " + hmnth + " " + "($" + str(chgup) + ")")
    print("Greatest Decrease in Profits:  " + lmnth + " " + "($" + str(chgdwn) + ")")
    
    file.write("Finanancial Analysis" +"\n")
    file.write("-----------------------------------------" + "\n")
    file.write("Total Months: " + str(len(months) + 1) +"\n")
    file.write("Total: $" + str(dollarsum) +"\n")
    file.write("Average Change: $" + str(round(avgchange, 2)) +"\n")
    file.write("Greatest Increase in Profits:  " + hmnth + " " + "($" + str(chgup) + ")" +"\n")
    file.write("Greatest Decrease in Profits:  " + lmnth + " " + "($" + str(chgdwn) + ")")
