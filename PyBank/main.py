import csv
import os

def output_data(bDict, mAvg, fMax, mxMon, fMin, miMon):
    header1 = "Finanical Analysis"
    header2 = "---------------------------------------"
    outFile = open("Finanical_analysis.txt", 'w')
    outFile.write(header1 + "\n")
    print(header1)
    outFile.write(header2 + "\n")
    print(header2)
    outFile.write("Total Months: " + str(len(bDict)) + "\n")
    print("Total Months: " + str(len(bDict)))
    outFile.write("Total: $" + str(sum(bDict.values())) + "\n")
    print("Total: $" + str(sum(bDict.values())))
    outFile.write("Average Change: $" + str(round(sum(mAvg) / len(mAvg),2)) + "\n")
    print("Average Change: $" + str(round(sum(mAvg) / len(mAvg),2)))
    outFile.write("Greatest Increase in Profits: " + mxMon + " ($" + str(fMax) + ")\n")
    print("Greatest Increase in Profits: " + mxMon + " ($" + str(fMax) + ")")
    outFile.write("Greatest Decrease in Profits: " + miMon + " ($" + str(fMin) + ")\n")
    print("Greatest Decrease in Profits: " + miMon + " ($" + str(fMin) + ")")
    outFile.close()
    return


bankPath = os.path.join("budget_data.csv")
total = 0
bankDict = {}
lastMon = 0
monAvg = []
finMax = 0
finMin = 10000000

with open(bankPath, newline = '') as csvfile:
    csvReader = csv.reader(csvfile, delimiter = ",")
    next(csvReader, None)
    for row in csvReader:
        bankDict[row[0]] = int(row[1])
        monChange = int(row[1]) - lastMon
        if (monChange > finMax):
            finMax = monChange
            maxMon = row[0]
        if (monChange < finMin):
            finMin = monChange
            minMon = row[0]
        if (lastMon != 0):
            monAvg.append(monChange)
        lastMon = int(row[1])
    output_data(bankDict, monAvg, finMax, maxMon, finMin, minMon)