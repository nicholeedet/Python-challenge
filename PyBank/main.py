import os 
import csv
# Declare file location through csvpath
csvpath = os.path.join( 'Resources', 'budget_data.csv')
print(csvpath)

# Define list to represent data variable
total_months = []
total_profit = []
Average_profit_change = []

# Open csv with Improved Reading using CSV module
with open(csvpath, newline="", encoding="utf-8") as budget:
    
 # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(budget,delimiter=",") 

    header = next(csvreader)  
    for row in csvreader: 

        # Assign total months and total profit to their defined lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        Average_profit_change.append(total_profit[i+1]-total_profit[i])
        
        
# Find value for max and min of the the montly profit change list
max_increase_value = max(Average_profit_change)
max_decrease_value = min(Average_profit_change)
max_increase_month = Average_profit_change.index(max(Average_profit_change)) + 1
max_decrease_month = Average_profit_change.index(min(Average_profit_change)) + 1 


# Test your function with the following:
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(Average_profit_change)/len(Average_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")