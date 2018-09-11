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
        
        #     max_month_year_index = mom_dif.index(max_mom_dif)

        # if(max_month_year_index == profit_loss.index):
        #     max_pnl = profit_loss(max_month_year_index)

        # if(max_pnl == row[1]):
        #     max_month_year = row[0]
        
##calculate the max and min date and output as a string
       #max_cf_change_date = str(date[cf_change.index(max(cf_change))])


        #min_month_year = mom_dif.index(min_mom_dif)


print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {num_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_mom_dif}")
print(f"{max_month_year} {max_mom_dif}")
print(min_mom_dif)(max)