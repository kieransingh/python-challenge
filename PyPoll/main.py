import os
import csv


# Identifies file with poll data
csvpath = os.path.join('election_data_1.csv')

#Creates dictionary to be used for candidate name and vote count.
poll = {}
total_votes = 0
candidates = []
vote_count = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)

    #create a dictionary to store name and keep track of vote counts
    for row in csvreader:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 

#takes dictionary keys and values and puts the values into the lists
for key, value in poll.items():
    candidates.append(key)
    vote_count.append(value)

# creates vote percent list
vote_percent = []
for x in vote_count:
    vote_percent.append(round(x/total_votes*100, 1))

zipped_list = list(zip(candidates, vote_count, vote_percent))

winner_list = []

for name in zipped_list:
    if max(vote_count) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]

output_file = os.path.join('Output', 'Results.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Poll Results\n')
    txtfile.writelines("-------------------------\n")
    txtfile.writelines('Total Votes:' + str(total_votes)+ '\n')
    txtfile.writelines('-------------------------\n')
    for stat in zipped_list:
        txtfile.writelines(stat[0] + ": " + str(stat[2]) +'%  (' + str(float(stat[1])) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')
    


with open(output_file, 'r') as readfile:
    print(readfile.read())
