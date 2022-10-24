import os
import re
dir_path = r'./find_the_flag'
res = []
for path in os.listdir(dir_path): 
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
res.sort()
for i in res:
    file_name = './find_the_flag/' + i
    lines = open(file_name, 'r').read()
    word = re.split(r'\s+', lines)
    if len(word[0]) == 1:
        print(word[0], end = '')
print()
