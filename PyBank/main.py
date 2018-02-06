import os
import csv
csvpath = os.path.join('budget_data_1.csv')

#Empty lists to hold values
revenue = []
months = []


# with open(csvpath, 'r') as csvfile:
# with open(csvpath, newline = '') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter = ',')

#     next(csvreader, None)

# 	#loop thru each row
# 	for row in csvreader:
# 		months.append(row[0])
# 		revenue.append(int(row[1]))

with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))

#Total months		
total_months = len(months)

#find greatest increase and decrease
greatest_inc = revenue[0]
greatest_dec = revenue[0]
total_revenue = 0

for x in range(len(revenue)):
	if revenue[x] >= greatest_inc:
		greatest_inc = revenue[x]
		greatest_inc_mon = months[x]
	elif revenue[x] <= greatest_dec:
		greatest_dec = revenue[x]
		greatest_dec_mon = months[x]
	total_revenue += revenue[x]

#need to get average change
avg_change = round(total_revenue/total_months, 2)


#Create output file
output_file = os.path.join('Output','PyBank_out1.txt')
with open(output_file, 'w') as writefile:
	writefile.writelines('Financial Analysis\n')
	writefile.writelines('---------------------------------' + '\n')
	writefile.writelines('Total Months: ' + str(total_months) + '\n')
	writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
	writefile.writelines('Average Revenue Change: $' + str(avg_change) + '\n')
	writefile.writelines('Greatest Increase in Revenue: ' + greatest_inc_mon + ' ($' + str(greatest_inc) + ')'+ '\n')
	writefile.writelines('Greatest Decrease in Revenue: ' + greatest_dec_mon + ' ($' + str(greatest_dec) + ')')

with open(output_file, 'r') as readfile:
	print(readfile.read())
