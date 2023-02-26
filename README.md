# python-challenge
On this challenge i worked with multiple csv that contains lots of datasets and one of the dataset is 'election csv'
i needed to figure out the total votes of the election results and % of the votes each candidate won and total number of votes and lastly had to state the winner of the election
''' python
names = ["Charles Casper Stockham" ,"Diana DeGette" , "Raymon Anthony Doane"]
    def winner(votes): #finding the winner 
      vote_counts = [votes[name] for name in names]
      max_vote_count = max(vote_counts) # highest vote counts 
      winners =[name for name , count in votes.items() if count == max_vote_count]
      winner_name = winners [0]
      print(f"winner is: {winner_name} with {max_vote_count}")
    winner(votes)
'''
    with this code i tried finding the winner of this election which clearly Diana DeGette with 272892 of total vote but somehow its coming out winner as Charles with 1 vote. i think My logic is right but i'm missing something or i'm calculating wrong. 