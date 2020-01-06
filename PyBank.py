import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Instructions', 'PyBank', 'Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    Dates=[] #initialize list of dates
    Profit=[] #initialize list of profits
    Dprofit=[] #initialize list of change in profit
    totalp=0
    High=0
    Low=0
    
    # Loop through the data
    for row in csvreader:
        date=row[0] 
        pl=int(row[1]) #needs to be converted to numbers for calculations later
        Dates.append(date) #add each date to a list of dates
        Profit.append(pl) #add each value to a list of profits
        totalp += int(pl) #cumulatively add onto total sum of profits

    for i in range(1, len(Profit)): #start iterating at second element
        Dpl=int(Profit[i] - Profit[i-1]) #Dpl = Change in P/L
        Dprofit.append(Dpl)
        if Dpl>High: #Set greatest increase variables
            High = Dpl
            HighMonth = Dates[i]
        if Dpl<Low: #Set greatest decrease variables
            Low = Dpl
            LowMonth = Dates[i]       
        
AveChange = round((sum(Dprofit) / len(Dprofit)), 2) #Calculate Average Change

#print data to the terminal
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {len(Profit)}')
print(f'Total: ${sum(Profit)}')
print(f'Average Change: ${AveChange}')      
print(f'Greatest Increase in Profits: {HighMonth} ({High})')
print(f'Greatest Decrease in Profits: {LowMonth} ({Low})')

#Export Same data as above in text file
FA=open("Financial Analysis.txt", "w+") #opens file (or creates one if needed)
FA.write('Financial Analysis\n') #\n indicates to move down to the next line
FA.write('----------------------------\n')
FA.write(f'Total Months: {len(Profit)}\n')
FA.write(f'Total: ${sum(Profit)}\n')
FA.write(f'Average Change: ${AveChange}\n')
FA.write(f'Greatest Increase in Profits: {HighMonth} ({High})\n')
FA.write(f'Greatest Decrease in Profits: {LowMonth} ({Low})\n')
FA.close()
