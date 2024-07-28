#!/usr/bin/env python3

"""

 File: docsExamined.py
 Author: Dennis Spera
 Date: 2024-06-24
 Description: count of commands.
 Description: 
  1.) sort keysExamined from mongod.log(s) on stdin.

 Change Log:
  1. 2024-06-24 - Initial 

 Testing: 
  1. Not defined
"""

import json, sys
from collections import Counter
import json as j

jsonFile = list()

for line in sys.stdin:
    jsonFile.append( j.loads(line))
sys.stdin.close()

keysExamined = list()
sorted_list = list()
for json in jsonFile:
    if json['c'] == 'COMMAND':
       try:
        keysExamined.append({'json':j.dumps(json),'keysExamined':json['attr']['keysExamined']})
       except:
        pass
       
try:       
  sorted_list = sorted(keysExamined, key=lambda x: x['keysExamined'], reverse=True)
except:
  pass

if sorted_list:
   for element in sorted_list:
       print(element['json']) 
