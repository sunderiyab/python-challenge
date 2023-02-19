import os
import csv

csvpath = os.path.join("..", "resources", "budget_data.csv")

with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #file includes header
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    #The total number of months included in the dataset
    months = set()
    for row in csvreader:
        months.add(row[0])

    total_months = len(months)
    print(f'total months: {total_months}')

#The net total amount of "Profit/Losses" over the entire period
    csvfile.seek(0) #pointing to the back to beginning
    next(csvreader) #excludes header
    profit_losses = set()
    for row in csvreader:
        profit_losses.add(int(row[1]))

    net_total = sum(profit_losses)
    print(f'Net Total: {net_total}')

#The greatest increase in profits (date and amount) over the entire period
    csvfile.seek(0) #pointing to the back to beginning
    next(csvreader) #excludes header
    max_increase = 0 #setting up the variables
    max_increase_date = ""
    previous_profit_losses = None

    for row in csvreader:    #loops
        date = row[0]
        profit_loss = int(row[1])
        if previous_profit_losses is not None:
            increase = profit_loss - previous_profit_losses
            if increase > max_increase:
                max_increase = increase
                max_increase_date = date
        previous_profit_losses = profit_loss
    print(f"greatest increase in profits: {max_increase_date} + (${max_increase})")


#The greatest decrease in profits (date and amount) over the entire period
    csvfile.seek(0) #pointing to the back to beginning
    next(csvreader) #excludes header
    min_decrease = 0
    min_decrease_date = ""
    previous_profit_losses = None

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        if previous_profit_losses is not None:
            decrease = profit_loss - previous_profit_losses
            if decrease < min_decrease:
                min_decrease = decrease
                min_decrease_date = date
        previous_profit_losses = profit_loss
    print(f"greatest decrease in profits: {min_decrease_date} - (${min_decrease})")

    profit_loss = 0
    total_changes = 0
    changes = 0
    current_loss = 0
    for row in csvreader:
        current_loss = int(row[1])
        if profit_loss != 0:
           difference = current_loss - profit_loss
           total_changes += difference
           changes += 1
    profit_loss = current_loss
    average_change = total_changes / (changes +1)
    print(f'total_change: {total_changes}')
    print(f'average_change:{average_change}')
#something is off with my code it giving me 0