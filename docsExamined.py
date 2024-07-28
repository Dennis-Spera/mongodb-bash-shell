#!/usr/bin/env python3

"""

 File: docsExamined.py
 Author: Dennis Spera
 Date: 2024-06-24
 Description: count of commands.
 Description: 
  1.) sort docsExamined from mongod.log(s) on stdin.

 Change Log:
  1. 2024-06-24 - Initial 

 Testing: 
  1. Not defined
"""

import json, sys
import json as j

jsonFile = list()

for line in sys.stdin:
    jsonFile.append( j.loads(line))
sys.stdin.close()

docsExamined = list()
sorted_list = list()
for json in jsonFile:
    if json['c'] == 'COMMAND':
       try:
        docsExamined.append({'json':j.dumps(json),'docsExamined':json['attr']['docsExamined']})
       except:
        pass
       
try:       
  sorted_list = sorted(docsExamined, key=lambda x: x['docsExamined'], reverse=True)
  for element in sorted_list:
       print(element['json']) 
except:
  print('no queries with "docsExamined" could be found for the date range')
