import pandas as pd
import json, csv, os
import glob, os
import pandas as pd




os.chdir("/home/kami/Desktop/intern/file json")
for file in glob.glob("*.json"):
    with open(file) as json_file:
        data = json.load(json_file)
    employee_data = data['emp_details']
    name = file.split('.')[0]
    data_file = open(name+'.csv', 'w')
    csv_writer = csv.writer(data_file)
    count = 0
    for emp in employee_data:
        if count == 0:
            header = emp.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(emp.values())
    data_file.close()
    print(file)
os.chdir("/home/kami/Desktop/intern/file csv")
for file in glob.glob("*.csv"):
    name1 = file.split('.')[0]
    df = pd.read_csv (file)
    df.to_json (name1+'.json')




















# import pandas as pd
# df = pd.read_csv (r'/home/kami/Desktop/intern/data_file.csv')
# df.to_json (r'/home/kami/Desktop/intern/data_file.json')
