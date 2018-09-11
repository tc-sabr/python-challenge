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

unique_candidates = sorted(list(set(candidates)))

candidate_votes = Counter(candidates)

print(candidate_votes)

# def candidate_list(dictionary, target_keys):
#     return {key: dictionary[key] for key in target_keys}


#https://stackoverflow.com/questions/5904969/how-to-print-a-dictionarys-key
#look through candidates column

#get name and find index number

#take index number to use in adding to tally

#find corresponding index in the tally list

#add 1 to found

##once through loop calculate percentages

#votes for candidate 1 / total stored in list

#votes for candidate 2 / total stored in list

#votes for candidate 3 / total stored in list

#votes for candidate 4 / total stored in list

#print header
print("Election Results")
print("---------------------------------")

#print total votes
print(f"Total Votes: {total_votes}")
print("---------------------------------")

for key, value in candidate_votes.items():
    percent = round((value / total_votes) * 100, 2)
    print(f"{key} {percent}% ({value})")
# #print candidate name: % of votes (#votes)
# for candidate_index in range(len(unique_candidates)):
#     vote_name = str(unique_candidates[candidate_index])
#     #vote_percent = str(candidate_vote_percent[candidate_index])
#     vote_count = str(candidate_votes[candidate_index])

# print(f"{vote_name}: {vote_count} votes")
# #print(f"{vote_name}: {vote_percent} ({vote_count})")
print("---------------------------------")

#print winner
#zip candidates & votes
# zip_results = dict(zip(candidate_votes, unique_candidates))

# # #max in vote count
# winner = max(candidate_votes)

# # #print winner name
# print(f"Winner: {zip_results[winner]}")




    #for row in csvreader:

        #if([unique_candidates] == row[2]):

            

#look through candidate column

#add 1 to corresponding index
                
    #append candidates if name not already in there
    #name = row[2]
    #if name not in [candidates]:
    # candidates.append(name)

#vote_index = int(candidates) - 1

#candidate_votes[vote_index] += 1



#print(unique_candidates)

