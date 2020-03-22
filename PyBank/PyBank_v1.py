import os
import csv

pybank_csv = os.path.join("budget_data.csv")

# Open and read csv
with open(pybank_csv) as csvfile:
# Read the file as csv file
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    #The total number of months included in the dataset
    total_month = 0
    #The net total amount of "Profit/Losses" over the entire period
    total_amount = 0
    #The average of the changes in "Profit/Losses" over the entire period
    profit_losses_change = 0
    previous_profit_losses = 0
    month_change = []
    #The greatest increase in profits (date and amount) over the entire period
    profit_losses_change_list = []
    greatest_increase = ["", 0]
    #The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = ["", 99999999999]

    for row in csvreader:
        total_month = total_month+1
        total_amount = total_amount + int(row[1])
        
        profit_losses_change = int(row[1]) - previous_profit_losses
        previous_profit_losses = int(row[1])
        month_change = month_change + [row[0]]
        profit_losses_change_list = profit_losses_change_list + [profit_losses_change]

        if (profit_losses_change > greatest_increase[1]):
            greatest_increase[1] = profit_losses_change
            greatest_increase[0] = row[0]
        
        if (profit_losses_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_losses_change

#for some reason I can not figure out the average so I have have left the two I attempted below

#average = sum(profit_losses_change_list)/len(profit_losses_change_list)
#average= total_amount/(total_month-1)
        
print(total_month)
print(total_amount)
print(average)
print(greatest_increase[1])
print(greatest_decrease[1])