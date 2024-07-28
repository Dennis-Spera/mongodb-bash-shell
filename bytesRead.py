#!/usr/bin/env python3

"""

 File: bytesRead.py
 Author: Dennis Spera
 Date: 2024-06-24
 Description: 
  1.)  Description: sort bytesRead from mongod.log(s) on stdin.

 Change Log:
  1. 2024-06-24 - Initial 
  2. 2024-07-17 - reworded comments, removed unused modules

 Testing: 
  1. Not defined
"""

import json, sys
import json as j

jsonFile = list()

for line in sys.stdin:
    jsonFile.append( j.loads(line))
sys.stdin.close()

bytesRead = list()
for json in jsonFile:
    if json['c'] == 'COMMAND':
      try:
        bytesRead.append({'json':j.dumps(json),'bytesRead':json['attr']['storage']['data']['bytesRead']})
      except:
       pass
       
try:       
 sorted_list = sorted(bytesRead, key=lambda x: x['bytesRead'], reverse=True)

 for element in sorted_list:
     print(element['json']) 
except:
   sys.stderr.write('No useable data found'+"\n")