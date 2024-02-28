import csv
import json
import pandas as pd


def export(fmt):
    if fmt == 'CSV':
        with open("outputTemp.csv", 'r') as r, open('output.csv', 'w') as o:
            for line in r:
                # strip() function
                if line.strip():
                    o.write(line)

    if fmt == 'EXCEL':
        with open("outputTemp.csv", 'r') as r, open('output.csv', 'w') as o:
            for line in r:
                # strip() function
                if line.strip():
                    o.write(line)
        read_file = pd.read_csv('output.csv')
        read_file.to_excel('output.xlsx', index=None, header=True)

    if fmt == 'JSON':
        with open("outputTemp.csv", 'r') as r, open('output.csv', 'w') as o:
            for line in r:
                # strip() function
                if line.strip():
                    o.write(line)

        csvFilePath = r'output.csv'
        jsonFilePath = r'output.json'

        jsonArray = []

        # read csv file
        with open(csvFilePath, encoding='utf-8') as csvf:
            # load csv file data using csv library's dictionary reader
            csvReader = csv.DictReader(csvf)

            # convert each csv row into python dict
            for row in csvReader:
                # add this python dict to json array
                jsonArray.append(row)

        # convert python jsonArray to JSON String and write to file
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonString = json.dumps(jsonArray, indent=4)
            jsonf.write(jsonString)

    else:
        with open("outputTemp.csv", 'r') as r, open('output.txt', 'w') as o:
            for line in r:
                # strip() function
                if line.strip():
                    o.write(line)
