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
   
#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote

