# Create a Python script that analyzes the PyBank records to calculate each of the following:
# -->>  The total number of months included in the dataset
# -->>  The net total amount of "Profit/Losses" over the entire period
# -->>  The average of the changes in "Profit/Losses" over the entire period
# -->>  The greatest increase in profits (date and amount) over the entire period
# -->>  The greatest decrease in losses (date and amount) over the entire period
# -->>  Print the analysis to the terminal and export a text file with the results

# Import files
import os
import csv

# Define Pybank's 
months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# Change directory to the current python script
os.chdir(os.path.dirname(main.py))

# Path collect data
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

# Open the csv & read the csv
with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header
    csv_header = next(csvfile)

    # print(f"Header:{csv_header}")
    #Printes --> Header: Date, Profit/Losses

    # Count of the months
    count_months += 1

    #Net total amount of "Profits/Losses"over the whole period
    current_month_profit_loss = int(row[1])
    net_profit_loss += current_month_profit_loss

    if (count_months == 1):
    #Make the vaile of previous month to be the current month
    previous_month_profit_loss = current_month_profit_loss

    else:

    # Compute change in the profit loss
    previous_month_profit_loss = current_month_profit_loss

    # Append each month to the months[]
    months.append(row[0])

    # Append each profit_loss_change to the profit_loss_changes[]
    profit_loss_changes.append(profit_loss_change)

    # Make the current month to be previous month for next loop
    previous_month_profit_loss = current_month_profit_loss

    # sum and average of the changes in Profit & Losses
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months -1), 2)

    # hightest & lowest changes in Profit & losses 
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate index value of the highest and lowest changes
    highest_month_index = profit_loss_change.index(highest_change)
    lowest_month_index = profit_loss_change.index(lowest_change)

    # Assign best & worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_profit_loss}")
print(f"Greatest Increase in Profits: {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses: {worst_month} (${lowest_change}")

# Export a text file with the results
budgest_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")

