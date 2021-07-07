#PyBank 
#Load CSV file and insure it prints to terminal 

import os 
import csv

# Open the budget CSV in read mood. 
csvpath = os.path.join('.', 'Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',') 
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
     
    # Outline variables for Pybank 
    months = []
    change_profit_or_lose = []
    total_number_months = 0
    last_month_outcome = 0
    current_month_outcome = 0 
    Over_all_change = 0
    total_net_profit_lose = 0 

    for row in csvreader:
        #Sum the number of months: 
        total_number_months += 1 
        
        #total net amout of profit or lose.
        current_month_outcome = int(row[1])
        total_net_profit_lose += current_month_outcome

        #Sum all values to get over all value: 
        sum_profit_loss = sum(change_profit_or_lose)
        #Outlining the markers to work out profit or loss 
        if (total_number_months == 1 ): 
            last_month_outcome = current_month_outcome
            continue
        else: 
            Over_all_change = current_month_outcome - last_month_outcome
            months.append(row[0])   
            change_profit_or_lose.append(Over_all_change)
            last_month_outcome = current_month_outcome
    #Outline the biggest / smallest changes in profit 
    biggest_change = max(change_profit_or_lose)
    Smallest_change = min(change_profit_or_lose)
    # Work out the best months and assign index 
    highest_month_index = change_profit_or_lose.index(biggest_change)
    lowest_month_index = change_profit_or_lose.index(Smallest_change)

    #Define the best and worst months from the data sheet. 
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# Print to terminal: 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {total_number_months}")
print(f"Total:  ${total_net_profit_lose}")
print(f"Greatest Increase in Profits:  {best_month} (${biggest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${Smallest_change})")

# create new txt file and print the outcomes:
finacial_analysis_file = os.path.join('.', 'analysis','finacial_analysis.txt')
with open(finacial_analysis_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {total_number_months}\n")
    outfile.write(f"Total:  ${total_net_profit_lose}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${biggest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${Smallest_change})\n")

