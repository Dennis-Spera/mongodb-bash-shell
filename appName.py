#!/usr/bin/env python3

"""

 File: appName.py
 Author: Dennis Spera
 Date: 2024-06-24
 Description: 
  1.) Extract appName totals from mongod.log on stdin.
  2.) appnames will be both user and system appnames.

 Change Log:
  1. 2024-06-24 - Initial

 Testing: 
  1. Not defined
"""

import json, sys
from collections import Counter

jsonFile = list()

for line in sys.stdin:
    data = json.loads(line)
    jsonFile.append(data)

sys.stdin.close()

appNames = list()
for json in jsonFile:
    if json['c'] == 'COMMAND':
       try:
        appNames.append({json['attr']['appName']:1})
       except:
        pass    

result = Counter(key for d in appNames for key in d)
sorted_result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

print("{:>10}   {:<10}".format('Count', 'App Name'))
print("{:>10}   {:<10}".format('-----', '----------------------'))

for k,v in sorted_result.items():
    print("{:>10}   {:<10}".format(v, k))