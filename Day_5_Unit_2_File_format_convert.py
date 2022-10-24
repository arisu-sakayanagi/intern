import json, csv, argparse
import pandas as pd
from openpyxl import Workbook

parser = argparse.ArgumentParser()
parser.add_argument('--input','--input', type=str, help='input file name')
parser.add_argument('--output','--output', type=str, help='output file name')
parser.add_argument('-jsontocsv', '--result', action='store_true', help='json to csv')
parser.add_argument('-jsontoxlsx', '--result1', action='store_true', help='json to xlsx')

args = parser.parse_args()
if args.result:
    with open(args.input) as json_file:
        data = json.load(json_file)
    employee_data = data['emp_details']
    data_file = open(args.output, 'w')
    csv_writer = csv.writer(data_file)
    count = 0
    for emp in employee_data:
        if count == 0:
            header = emp.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(emp.values())
    data_file.close()
    print('Successfully json to csv file')
if args.result1:
    with open(args.input) as json_file:
        data = json.load(json_file)
    employee_data = data['emp_details']
    data_file = open('data.csv', 'w')
    csv_writer = csv.writer(data_file)
    count = 0
    for emp in employee_data:
        if count == 0:
            header = emp.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(emp.values())
    data_file.close()
    wb = Workbook()
    ws = wb.active
    with open('data.csv', 'r') as f:
        for row in csv.reader(f):
            ws.append(row)
    wb.save('data.xlsx')
    print('Successfully json to xlsx file')













# import json, csv, argparse


# parser = argparse.ArgumentParser()
# parser.add_argument('--input','--input', type=str, help='input file name')
# parser.add_argument('--output','--output', type=str, help='output file name')
# args = parser.parse_args()

# with open(args.input) as json_file:
#     data = json.load(json_file)
# employee_data = data['emp_details']
# data_file = open(args.output, 'w')
# csv_writer = csv.writer(data_file)
# count = 0
# for emp in employee_data:
#     if count == 0:
#         header = emp.keys()
#         csv_writer.writerow(header)
#         count += 1
#     csv_writer.writerow(emp.values())
# data_file.close()
# print('Successfully created')







# import json
# import csv




# with open('data.json') as json_file:
#     data = json.load(json_file)
# employee_data = data['emp_details']
# data_file = open('data_file.csv', 'w')
# csv_writer = csv.writer(data_file)
# count = 0
# for emp in employee_data:
#     if count == 0:
#         header = emp.keys()
#         csv_writer.writerow(header)
#         count += 1
#     csv_writer.writerow(emp.values())
# data_file.close()





