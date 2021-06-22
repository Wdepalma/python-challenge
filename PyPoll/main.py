import os
import csv

Total_Votes = 0
candidates = []
Votes = []
Cand_w_votes = []
Cand_v_count = []
Cand_v_percent = []
vote_tally = []
tally = {}
vcount = 0
maxcount = 0
percent_count = 0.0

filepath = "Resources/election_data.csv"
with open(filepath) as election :
    datalist = csv.reader(election, delimiter=',')
  
    csv_header = next(datalist)
    #print(f"CSV Header: {csv_header}")
    
    for row in datalist:
        Total_Votes = Total_Votes + 1
        Votes.append(row[2])
        if candidates.count(row[2]) == 0 :
            candidates.append((row[2]))



tv = format(Total_Votes,",")

for  name in candidates:
    tally.update({name:Votes.count(name)})
    vcount = (Votes.count(name))
    percent_count = (vcount / Total_Votes)

    fmt_vcount = format(vcount,",")
    fmt_percent_count = format(percent_count,".2%")    

    Cand_w_votes.append(name)
    Cand_v_count.append(fmt_vcount)
    Cand_v_percent.append(fmt_percent_count)

    if vcount > maxcount :
        maxcount = vcount
        winner = name
  

vote_tally = zip(Cand_w_votes,Cand_v_count,Cand_v_percent)

outpath = "Analysis/Election_Results.csv"
with open(outpath,'w',newline='') as csvfile :
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results:"])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow(["Total Votes = ",tv])
    csvwriter.writerow(["The winner is ",winner])
    csvwriter.writerow(["---------------------------------"])
    csvwriter.writerow(["Candidate","Vote Count","Percent of Total"])
    csvwriter.writerows(vote_tally)
    
print("Election Results:")
print("---------------------------------")
print(f"Total Votes = {tv}")
print("The winner is " + winner)
print("---------------------------------")

vote_tally = zip(Cand_w_votes,Cand_v_count,Cand_v_percent)
for row in vote_tally:
    print(row[0],row[1],row[2])
print("=================================")



