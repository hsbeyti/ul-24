import csv
import sys
import json

from common.CommonFunctions import CommonFunctions

def prepareData(filename, outputFilename):
    commonFunctions = CommonFunctions("../../")
    data = commonFunctions.openFileForReadOnly(filename)
    output = commonFunctions.openFileForWriting(outputFilename)
    my_empty_list = []
    binaryIndex = 1
    sum = 0
        # Create a CSV reader object
    csv_reader = csv.reader(data['data'], delimiter=',')
    csv_writer = csv.writer(output['data'])
    for row in csv_reader:
        if row[0] == '1':
            my_empty_list.append("#######################")
            csv_writer.writerow(my_empty_list)
            my_empty_list.clear()
            continue
        
        if row[0] == '#':
            my_empty_list.append("\t\tbinary "+str(binaryIndex))
            csv_writer.writerow(my_empty_list)
            my_empty_list.clear()
            binaryIndex += 1
            continue

        my_empty_list.append(row[0])
       
        for j in range(4, len(row)):

            sum += int(row[j]) if row[j] else 0
            continue

        my_empty_list.append(str(sum))
        csv_writer.writerow(my_empty_list)
        my_empty_list.clear()
        sum = 0



        
prepareData("input/readyForML.csv", "output/output.csv")




