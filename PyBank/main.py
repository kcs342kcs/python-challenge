import csv
import os

def avgDiff(c, p, l ):
    if(p != 0):
        if((c < 0) or (p < 0)):
            l.append(c + p)
        elif(c >= p):
            l.append(c - p)
        else:
            l.append(p - c)
    return

def output_data(bDict, mAvg, tot):
    header1 = "Finanical Analysis"
    header2 = "---------------------------------------"
    key_max = max(bDict.keys(), key=(lambda k: bDict[k]))
    key_min = min(bDict.keys(), key=(lambda k: bDict[k]))
    outFile = open("Finanical_analysis.txt", 'w')
    outFile.write(header1 + "\n")
    print(header1)
    outFile.write(header2 + "\n")
    print(header2)
    outFile.write("Total Months: " + str(len(bDict)) + "\n")
    print("Total Months: " + str(len(bDict)))
    outFile.write("Total: $" + str(tot) + "\n")
    print("Total: $" + str(tot))
    outFile.write("Average Change: $" + str(round(sum(mAvg) / len(mAvg),2)) + "\n")
    print("Average Change: $" + str(round(sum(mAvg) / len(mAvg),2)))
    outFile.write("Greatest Increase in Profits: " + key_max + " ($" + str(bDict[key_max]) + ")\n")
    print("Greatest Increase in Profits: " + key_max + " ($" + str(bDict[key_max]) + ")")
    outFile.write("Greatest Decrease in Profits: " + key_min + " ($" + str(bDict[key_min]) + ")\n")
    print("Greatest Decrease in Profits: " + key_min + " ($" + str(bDict[key_min]) + ")")
    outFile.close()
    return


bankPath = os.path.join("budget_data.csv")
total = 0
bankDict = {}
lastMon = 0
monAvg = []

with open(bankPath, newline = '') as csvfile:
    csvReader = csv.reader(csvfile, delimiter = ",")
    next(csvReader, None)
    for row in csvReader:
        total = total + int(row[1])
        bankDict[row[0]] = int(row[1])
        avgDiff(int(row[1]), lastMon, monAvg)
        lastMon = int(row[1])
    output_data(bankDict, monAvg, total)