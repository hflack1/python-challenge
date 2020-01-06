#import dependencies
import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Instructions', 'PyPoll', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    Total=0 #initialize total votes
    header = next(csvreader)
    VoteTally = {} #initialize blank dictionary
    
    #Loop through the data
    for row in csvreader:
        Total += 1 #keep running total of votes
        Name = row[2] #set Name to name of each candidate as we read each vote
        if Name not in VoteTally: #Add candidate name to dictionary if not already there
            VoteTally.update({Name:1})
        else: #add one vote to candidate vote tally if candidate already exists
            t = VoteTally[Name] + 1 #t represents the new vote tally for this candidate
            VoteTally.update({Name:t}) #update the candidate's total votes

#Determine Winner of election
Winner=max(VoteTally, key=VoteTally.get)

#print election results to the terminal
print('Election Results')
print('-------------------------')
print(f'Total Votes: {Total}')
print('-------------------------')            
for Name, Tally in VoteTally.items(): #loop through each candidate and vote tally and print
    print(f'{Name}: {round((Tally/Total)*100,2)}% ({Tally})')
print('-------------------------') 
print(f'Winner: {Winner}')
print('-------------------------')

#Export Same data as above in text file
PP=open("Election Results.txt", "w+") #opens file (or creates one if needed)
PP.write('Election Results\n')
PP.write('-------------------------\n')
PP.write(f'Total Votes: {Total}\n')
PP.write('-------------------------\n')            
for Name, Tally in VoteTally.items():
    PP.write(f'{Name}: {round((Tally/Total)*100,3)}% ({Tally})\n')
PP.write('-------------------------\n') 
PP.write(f'Winner: {Winner}\n')
PP.write('-------------------------\n')
PP.close()