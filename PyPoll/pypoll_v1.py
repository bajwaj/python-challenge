import os
import csv

pypoll_csv = os.path.join("election_data.csv")
# The total number of votes cast
total_votes = 0

# A complete list of candidates who received votes
total_candidates = 0
candidates = []

# The percentage of votes each candidate won



# The total number of votes each candidate won



# The winner of the election based on popular vote.



# Open and read csv
with open(pypoll_csv) as csvfile:
# Read the file as csv file
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    for row in csvreader:
        total_votes = total_votes+1
        candidate = row[2]

        if candidate in candidates:
            candiates[candidate] = candidates[candidate] +1
        else:
            candidates[candidate] = 1
print(total_votes)






