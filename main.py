import numpy as np
import pandas as pd

## PyBank

data = pd.read_csv("budget_data.csv")

months = data['Profit/Losses'].count()
print(months)
total = data['Profit/Losses'].sum()
print(total)

data['diff'] = data['Profit/Losses'].diff()
changes = data['diff'].mean()
print(changes)

great_increase = 0
great_increase_date = ""
great_decrease = 0
great_decrease_date = ""

for row in data.itertuples():
    if row[3] > great_increase:
        great_increase = row[3]
        great_increase_date = row[1]
    if row[3] < great_decrease:
        great_decrease = row[3]
        great_decrease_date = row[1]

print(great_increase)
print(great_increase_date)
print(great_decrease)
print(great_decrease_date)

output = " Financial Analysis \n ---------------------------- \n Total Months: "
output = output + str(months) + "\n Total: $" + str(total)
output = output + "\n Average Change: $" + str(round(changes,2))
output = output + "\n Greatest Increase in Profits: " 
output = output + great_increase_date + " ($" + str(round(great_increase,0)) + ")"
output = output + "\n Greatest Decrease in Profits: "
output = output + great_decrease_date + " ($" + str(round(great_decrease,0)) + ")"
print(output)

file = open("PyBank.txt", 'w')
file.write(output)
file.close()


## PyPoll

data = pd.read_csv("election_data.csv")

total = data['Ballot ID'].count()
print(total)

result = pd.pivot_table(data, index='Candidate', values=['Ballot ID'], aggfunc='count')
result.head()

output = " Election Results\n -------------------------\n Total Votes: "
output = output + str(total) + "\n -------------------------"
winner = ""
winner_total = 0

for row in result.itertuples():
    output = output + "\n " + row[0] + ": " 
    output = output + str(round(row[1]/total,5)) + " (" +  str(row[1]) + ")"  
    if row[1] > winner_total:
        winner = row[0]
        winner_total = row[1]

output = output + "\n -------------------------\n Winner: " + winner + "\n -------------------------"
print(output)

file = open("PyPoll.txt", 'w')
file.write(output)
file.close()

