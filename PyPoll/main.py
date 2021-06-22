import os
import csv

Total_Votes = 0
candidates = []
Votes = []
x = 0
y = 0
j = 0


filepath = "Resources/election_data.csv"
with open(filepath) as election :
    datalist = csv.reader(election, delimiter=',')
  
    csv_header = next(datalist)
    print(f"CSV Header: {csv_header}")
    #first = next(datalist)
    #print(first[2])

    for row in datalist:
        Total_Votes = Total_Votes + 1
        Votes.append(row[2])
        if candidates.count(row[2]) == 0 :
            candidates.append((row[2]))



print(f"Total Votes = {Total_Votes}")

x = len(candidates)
print(x)
for  name in candidates:
    print(name)


j = len(Votes)
print(j)



y = candidates.count('Khan')
print(y)



