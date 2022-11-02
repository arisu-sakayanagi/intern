import subprocess, argparse, xlsxwriter, yaml
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', type=str, help='target')
parser.add_argument('-c', '--config', type=str, help='config')
parser.add_argument('sigma', metavar='sigma', type=str,help='sigma')
args = parser.parse_args()
sigma = args.sigma

query = subprocess.check_output('/home/kami/sigma/tools/sigmac -t'+args.target+' -c'+args.config+' '+sigma, shell=True).decode('utf-8')

file_name = sigma.split('/')[-1]
with open(sigma, "r") as stream:
    try:
        dict = yaml.safe_load(stream)
        title = dict['title']
        description = dict['description']
        technique = dict['tags']
    except yaml.YAMLError as exc:
        print(exc)

workbook = xlsxwriter.Workbook('sigma_to_excel.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'File Name')
worksheet.write('B1', 'Title')
worksheet.write('C1', 'Description')
worksheet.write('D1', 'Technique')
worksheet.write('E1', 'Query')
worksheet.write('B2', title)
worksheet.write('C2', description)
worksheet.write('A2', file_name)
worksheet.write('E2', query)
worksheet.write('D2', '\n'.join(technique))
workbook.close()
