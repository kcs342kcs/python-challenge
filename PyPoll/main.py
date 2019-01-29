import csv
import os

def output_data(vTotal):
    tot = 0
    outList = []
    key_max = max(vTotal.keys(), key=(lambda k: vTotal[k]))
    for votes in vTotal.keys():
        tot = tot + vTotal[votes]
    for per in vTotal.keys():
        p = '{0:.3f}'.format(vTotal[per] / tot * 100)
        inStr = str(per) + ": " + str(p) + "% (" + str(vTotal[per]) + ")"
        outList.append(inStr)
    lStr = max(outList, key = len)
    outFile = open("election_results.txt", 'w', newline = '')
    outFile.write("Election Results" + "\n")
    print("Election Results")
    outFile.write("-" * len(lStr) + "\n")
    print("-" * len(lStr))
    outFile.write("Total Votes: " + str(tot) + "\n")
    print("Total Votes: " + str(tot))
    outFile.write("-" * len(lStr) + "\n")
    print("-" * len(lStr))
    for line in outList:
        outFile.write(line + "\n")
        print(line)
    outFile.write("-" * len(lStr) + "\n")
    print("-" * len(lStr))
    outFile.write("Winner: " + str(key_max) + "\n")
    print("Winner: " + str(key_max))
    outFile.write("-" * len(lStr) + "\n")
    print("-" * len(lStr))
    return
        

csvPath = os.path.join("election_data.csv")
voteTotals = {}
with open(csvPath, newline = '') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")
    next(csvReader, None)
    for row in csvReader:
        if (str(row[2]) in voteTotals):
            voteTotals[str(row[2])] = voteTotals[row[2]] + 1
        else:
            voteTotals[str(row[2])] = 1
output_data(voteTotals)
