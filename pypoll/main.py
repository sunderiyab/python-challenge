#import the file 
import os
import csv
csvpath = os.path.join("..","resources", "election_data.csv")
with open (csvpath, "r" ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #file includes header
    csv_header = next(csvreader)
    #check to see if im opening the right file
    print(f"header: {csv_header}")

#The total number of votes cast
#init number of votes to integar value = 0
    number_of_votes = [] #empty list to store the votes
    for row in csvreader:
        vote = row[0]
        number_of_votes.append("vote")
    total_number = len(number_of_votes)
    print(f"total number of votes: {total_number}")
  #The total number of votes each candidate won
    csvfile.seek(0) #pointing to the back to beginning
    next(csvreader)
    number_of_votes = {
    "Charles Casper Stockham" : 0,
    "Diana DeGette": 0,
    "Raymon Anthony Doane" : 0 
    }
    for row in csvreader:
        candidates = row[2]
        if candidates == "Charles Casper Stockham":
            number_of_votes["Charles Casper Stockham"] += 1
        elif candidates == "Diana DeGette":
            number_of_votes["Diana DeGette"] +=1
        elif candidates == "Raymon Anthony Doane":
            number_of_votes["Raymon Anthony Doane"] +=1

    total_votes = sum(number_of_votes.values())

    print(f"Charles Casper Stockham: {number_of_votes['Charles Casper Stockham']}")
    print(f"Diana DeGette: {number_of_votes['Diana DeGette']}")
    print(f"Raymon Anthony Doane: {number_of_votes['Raymon Anthony Doane']}")
    #percentage of vote
    for candidates, count in number_of_votes.items():
        percentage =round(count/total_votes * 100, 3)
        print(f"{candidates} : {percentage}%")

        #winner
    csvfile.seek(0) #pointing to the back to beginning
    next(csvreader)
    votes = {}
    for row in csvreader:
        candidate = row[2]
        if candidate not in votes:
           votes[candidate] = 0 
        votes[candidate] += 1
        winner = max(votes, key=votes.get)
    print(f"Winner: {winner}") 


with open("pypoll_analysis.txt", "w") as file:
    file.write(f"total_votes: {total_votes}\n")
    file.write(f"candidates: ${number_of_votes}\n")