#!/usr/bin/env python3

"""

 File: millis.py
 Author: Dennis Spera
 Date: 2024-06-24

 Description: 
  1.) sort durationMillis from mongod.log(s) on stdin from highest durationMillii to lowest.
  2.) usage: {stdin} | millis -ge {durationMillis} [-ctx {context}] 
      a. if context is not specified will match all contexts

 Change Log:
  1. 2024-06-24 - Initial 
  2. 2024-07-14 - Additional error checking

 Testing: 
  1. Not defined
"""

import json, sys
import json as j
from commandlines import Command as cmd

ge = int()
c = cmd()
try:
 ge = int(c.get_definition('ge')) 
except:
 ge = int(0)

try:
 ctx = (c.get_definition('ctx')).upper() 
except:
 ctx = '_not_selected_'

jsonFile = list()

for line in sys.stdin:
    jsonFile.append( j.loads(line))
sys.stdin.close()

millis = list()
for json in jsonFile:
    if json['c'] == ctx or ctx == '_not_selected_':
       try:
        if int(json['attr']['durationMillis']) >= ge:
           millis.append({'json':j.dumps(json),'milli':json['attr']['durationMillis']})
       except:
        pass

try:       
 sorted_list = sorted(millis, key=lambda x: x['milli'], reverse=True)

 for element in sorted_list:
     print(element['json']) 
except:
     sys.stderr.write('No useable data found'+"\n")