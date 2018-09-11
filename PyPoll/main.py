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

with open("PyPoll_Results.txt", "w") as text_file:

    #print header
    print("Election Results", file=text_file)
    print("---------------------------------", file=text_file)

    #print total votes
    print(f"Total Votes: {total_votes}", file=text_file)
    print("---------------------------------", file=text_file)

    #print the candidate names, percent won and their vote total
    for key, value in candidate_votes.items():
        percent = round((value / total_votes) * 100, 2)
        print(f"{key} {percent}% ({value})", file=text_file)

    print("---------------------------------", file=text_file)

    #print winner
    print(f"Winner: {max(candidate_votes, key=candidate_votes.get)}", file=text_file)

    print("---------------------------------", file=text_file)