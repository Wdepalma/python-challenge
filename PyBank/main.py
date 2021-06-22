import os
import csv

filepath = "Resources/budget_data.csv"

Total = 0.0
Month_ct = 0
avgChange = 0.0
maxchange = 0.0
minchange = 0.0
Change = 0.0
nChange = 0.0


with open(filepath) as budget_data :
    datalist = csv.reader(budget_data, delimiter=',')
  
    csv_header = next(datalist)
    #print(f"CSV Header: {csv_header}")
    first = next(datalist)
    #print("First " + first[0] +" Net Change = "+first[1])
    Total = float(first[1])
    Month_ct = 1
    Change = float(first[1])
    maxMonth = first[0]
    minMonth = first[0]
    nChange = float(first[1])


    for  row in datalist :
        Month_ct = Month_ct + 1
        Total = Total + float(row[1])
        nChange = float(row[1]) - Change
        currentM = row[0]
       
        if nChange > maxchange :
            maxchange = nChange
            maxMonth = row[0]
           
            
        if nChange < minchange :
            minchange = nChange
            minMonth = row[0]
        Change = float(row[1])

     
avgChange = Total / Month_ct        
print("Financial Analysis")
print("---------------------")
print(f"Total Months =  {Month_ct}")
print(f"Total = ${Total}")
print(f"Average Monthly Change = ${avgChange}")
print(f"Greatest Increase in Profits: {maxMonth} (${maxchange})")
print(f"Greatest Decrease in Profits: {minMonth} (${minchange})")

outpath = "Analysis/Budget_Analysis.csv"
with open(outpath,'w',newline='') as csvfile :
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Total Months = ",Month_ct])
    csvwriter.writerow(["Total = ",Total])
    csvwriter.writerow(["Average Monthly Chage = ",avgChange])
    csvwriter.writerow(["Greatest Increase in Profits: ",maxMonth,maxchange])
    csvwriter.writerow(["Greatest Decrease in Profits: ",minMonth,minchange])




