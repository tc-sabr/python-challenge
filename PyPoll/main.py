#PyPoll
import os
import csv
from collections import Counter

csvpath = os.path.join('election_data.csv')

#create lists
voter_id_count = []
candidates = []

#list to track votes
candidate_votes = []

with open(csvpath, newline='') as csvfile:

    #specify delimiter and variable that holds
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    csv_header = next(csvreader)

    #read rows after header
    for row in csvreader:

        #append voter id count with voter id
        voter_id_count.append(row[0])

        #calculate count of voter id
        total_votes = len(voter_id_count)

        candidates.append(row[2])

candidate_votes = Counter(candidates)

#print header
print("Election Results")
print("---------------------------------")

#print total votes
print(f"Total Votes: {total_votes}")
print("---------------------------------")

for key, value in candidate_votes.items():
    percent = round((value / total_votes) * 100, 2)
    print(f"{key} {percent}% ({value})")

print("---------------------------------")

#print winner
#zip candidates & votes
# zip_results = dict(zip(candidate_votes, unique_candidates))

# # #max in vote count
# winner = max(candidate_votes)

# # #print winner name
# print(f"Winner: {zip_results[winner]}")