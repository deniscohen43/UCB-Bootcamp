import csv
import os
import operator

vote_csv = os.path.join("election_data.csv")

with open(vote_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    vote_count = []
    candidate_names = []
    candidate_votes = {}

    for row in csvreader:

        vote_count.append(row[0])

        if row[2] not in candidate_names:
            candidate_names.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1

winner = max(candidate_votes.items(), key=operator.itemgetter(1))[0]

print("Election Results")
print("----------------------------")
print(f"Total Votes: {len(vote_count)}")
print("----------------------------")
for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/len(vote_count))*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
print("----------------------------")
print(f"Winner: {winner}")
print("-------------------------")

with open('Election_Results', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Votes: " + str(len(vote_count)) + "\n")
    text.write("---------------------------------------\n")
    for candidate in candidate_votes:
        text.write(candidate + " " + str(round(((candidate_votes[candidate]/len(vote_count))*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("Winner: " + winner + "\n")
    text.write("---------------------------------------\n")

        