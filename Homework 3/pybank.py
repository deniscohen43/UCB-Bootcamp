import csv
import os

company_csv = os.path.join("budget_data.csv")

with open(company_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    month_count = []
    profit = []
    change = []

    for row in csvreader:
        
        month_count.append(row[0])

        profit.append(int(row[1]))

    for i in range(len(profit)-1):
        change.append(profit[i+1]-profit[i])

increase = max(change)
decrease = min(change)

month_increase = change.index(max(change))+1
month_decrease = change.index(min(change))+1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")

with open('Financial_Analysis', 'w') as text:
    text.write("Financial Analysis\n")
    text.write("----------------------------\n")
    text.write("Total Months: " + str(len(month_count)) + "\n")
    text.write("Total: $" + str(sum(profit)) + "\n")
    text.write("Average Change:" + str(round(sum(change)/len(change),2)) + "\n")
    text.write("Greatest Increase in Profits: " + month_count[month_increase] + " ($" + (str(increase)) + ")\n")
    text.write("Greatest Decrease in Profits: " + month_count[month_decrease] + " ($" + str(decrease) + ")\n")


    
    
        