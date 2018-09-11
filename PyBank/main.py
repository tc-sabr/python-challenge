#PyBank
import os
import csv

csvpath = os.path.join('budget_data.csv')

#create lists
months = []
profit_loss = []
mom_dif = []

with open(csvpath, newline='') as csvfile:

    #specify delimiter and variable that holds
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    csv_header = next(csvreader)

    #read rows after header
    for row in csvreader:

        #append list with months
        months.append(row[0])

        #calculate number of months
        num_months = len(months)

        #append list with PnL data
        profit_loss.append(float(row[1]))

        #calculate net total of PnL
        net_total = sum(profit_loss)

    
        
        #calculate MoM difference in PnL
    for i in range(1, len(profit_loss)):

        #append list to hold data
        mom_dif.append((profit_loss[i]) - (profit_loss[i-1]))

        #calculate average of list
        avg_mom_dif = round(sum(mom_dif) / len(mom_dif), 2)

        #find max MoM change
        max_mom_dif = max(mom_dif)

        #find min MoM change
        min_mom_dif = min(mom_dif)

        #find max date
        max_mom_dif_date = str(months[mom_dif.index(max(mom_dif)) + 1])

        #find min date
        min_mom_dif_date = str(months[mom_dif.index(min(mom_dif)) + 1])

    with open("PyBank_Analysis.txt", "w") as text_file:

        #print analysis to txt file
        print("Financial Analysis", file=text_file)
        print("---------------------------------", file=text_file)
        print(f"Total Months: {num_months}", file=text_file)
        print(f"Total: ${net_total}", file=text_file)
        print(f"Average Change: ${avg_mom_dif}", file=text_file)
        print(f"Greatest Increase in Profits: {max_mom_dif_date} (${max_mom_dif})", file=text_file)
        print(f"Greatest Decrease in Profits: {min_mom_dif_date} (${min_mom_dif})", file=text_file)

print(open('PyBank_Analysis.txt').read())