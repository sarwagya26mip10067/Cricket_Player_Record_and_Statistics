print("CRICKET PLAYER RECORD AND STATISTICS")
print("******")

#Role Refers to Batsman, Bowler or All Rounder 

name=input("Enter Your Favourite Player name: ")
team=input("Enter Palyer's team: ")
role=input("Enter Player's Role: ")
matches=int(input("Enter number of matches: "))


total_runs=0
total_balls=0
highest_score=0
fifties=0
hundreds=0

total_wickets=0
best_wickets=0



for i in range(matches):
    print()
    print("Match",i+1)
    
    runs=int(input("Enter Player's Runs: "))
    balls=int(input("Enter no. of balls faced: "))
    wickets=int(input("Enter no. of wickets taken: "))
    
    total_runs = total_runs + runs
    total_balls = total_balls + balls
    total_wickets = total_wickets + wickets
    
    if runs > highest_score:
        highest_score = runs

    if wickets > best_wickets:
        best_wickets = wickets

    if runs >= 50:
        fifties = fifties + 1

    if runs >= 100:
        hundreds = hundreds + 1
        
        
batting_average = total_runs/matches 

if total_balls > 0:
        strike_rate=(total_runs/total_balls)*100
else:
        strike_rate=0
        
runs_per_match = total_runs / matches
wickets_per_match = total_wickets / matches


print()
print("******")
print("PLAYER'S RECORD")
print("******")

print("Player Name: ", name)
print("Team: ", team)
print("Role: ", role)
print("Matches Played: ", matches)

print()
print("BATTING STATISTICS")
print("******")

print("Total Runs:", total_runs)
print("Highest Score:", highest_score)
print("Batting Average:", batting_average)
print("Strike Rate:", strike_rate)
print("Number of 50s:", fifties)
print("Number of 100s:", hundreds)

print()
print("BOWLING STATISTICS")
print("******")

print("Total Wickets:", total_wickets)
print("Best Wickets in One Match:", best_wickets)

print()
print("PERFORMANCE")
print("******")


if runs_per_match >= 40 and wickets_per_match >= 2:
    print("Overall Performance: Excellent")
    
elif runs_per_match >= 30 or wickets_per_match >= 1:
    print("Overall Performance: Good")
    
else:
    print("Overall Performance: Needs Improvement")
    
    
print()
print("******")
print("END OF PROGRAM")
print("******")



        