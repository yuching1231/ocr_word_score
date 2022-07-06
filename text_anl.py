import json
import os

filepath = os.path.join('D:\\', 'hwcode', 'Project', 'accounts')
counter = 1
text = []
for files in filepath:
    with open(filepath + '\\' + account + str(counter) + '.json', encoding='utf-8', mode='r') as f:
        text += json.load(f)
    counter += 1


print(text)

#print(text)
