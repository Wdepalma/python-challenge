import os
import csv

# Initialize variables
Total_Votes = 0
candidates = []
Votes = []
Cand_w_votes = []
Cand_v_count = []
Cand_v_percent = []
vote_tally = []
vcount = 0
maxcount = 0
percent_count = 0.0

#  Open election data file in Resources folder.
filepath = "Resources/election_data.csv"
with open(filepath) as election :
    datalist = csv.reader(election, delimiter=',')
  
    csv_header = next(datalist)

    # Discover names of candidates with at least 1 vote
    # Create list of candidate names with votes casts - candidates[]
    # Count total votes in the data file - Total_Votes then format with commas as variable tv
    for row in datalist:
        Total_Votes = Total_Votes + 1
        Votes.append(row[2])
        if candidates.count(row[2]) == 0 :
            candidates.append((row[2]))

tv = format(Total_Votes,",")
#  For each candidate in the list of candidate names, count number of votes received.  Calculate percentage of total vote.
for  name in candidates:
    #tally.update({name:Votes.count(name)})
    vcount = (Votes.count(name))
    percent_count = (vcount / Total_Votes)
        # Format vote counts with commas, and vote percent as a percentage %
    fmt_vcount = format(vcount,",")
    fmt_percent_count = format(percent_count,".2%")    
        # Create lists of candidate names, votes received, and calculated percentages
    Cand_w_votes.append(name)
    Cand_v_count.append(fmt_vcount)
    Cand_v_percent.append(fmt_percent_count)
        # Capture candidate with most votes.
    if vcount > maxcount :
        maxcount = vcount
        winner = name
#  Zip together lists of candidate names, votes received and calculated percentages into zip object.  
vote_tally = zip(Cand_w_votes,Cand_v_count,Cand_v_percent)
# Write election results to csv file in Analysis folder.
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

# Print election results to the terminal.    
print("Election Results:")
print("---------------------------------")
print(f"Total Votes = {tv}")
print("The winner is " + winner)
print("---------------------------------")

# Zip lists of candidate names, votes and percentages again to print to terminal.
vote_tally = zip(Cand_w_votes,Cand_v_count,Cand_v_percent)
for row in vote_tally:
    print(row[0],row[1],row[2])
print("=================================")
