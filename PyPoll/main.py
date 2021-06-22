import os
import csv

Total_Votes = 0
candidates = []
Votes = []
tally = {}
vcount = 0
maxcount = 0
percent_count = 0.0




filepath = "Resources/election_data.csv"
with open(filepath) as election :
    datalist = csv.reader(election, delimiter=',')
  
    csv_header = next(datalist)
    print(f"CSV Header: {csv_header}")
    
    for row in datalist:
        Total_Votes = Total_Votes + 1
        Votes.append(row[2])
        if candidates.count(row[2]) == 0 :
            candidates.append((row[2]))


print(f"Total Votes = {Total_Votes}")

for  name in candidates:
    tally.update({name:Votes.count(name)})
    vcount = Votes.count(name)
    percent_count = (vcount / Total_Votes) * 100
    if vcount > maxcount :
        maxcount = vcount
        winner = name
    
    print(f"{name} {vcount}, {percent_count}")
print("Winner is " + winner)



print(tally)
x = tally["Khan"]
print(x)



