import csv
import sys
import json

from src.common.CommonFunctions import CommonFunctions

sys.path.append('./src')

commonFunctions = CommonFunctions("../../")
data = commonFunctions.returnTheseData(True,"okay","Hello")
print(data)

def process_csv(input_file, output_file):
    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        with open(output_file, 'w', newline='\n') as output_csv:
            writer = csv.writer(output_csv)

            # Loop through each row in the CSV file
            for row in reader:
                # Check for the delimiter '#' indicating a new set of rows
                if row[0] == '#':
                    writer.writerow("########################")
                elif row[2] == '1' and row[0] != '1':
                    patterns = row[4:]
                    patterns_sum = sum(1 for val in patterns if val=='1')
                    # Write API name and sum of patterns to the output file
                    writer.writerow([row[0], patterns_sum])

    print("Processing complete. Output written to", output_file)


input_filename = '../../input/readyForML.csv'
output_filename = '../../output/output_data.csv'

process_csv(input_filename, output_filename)
