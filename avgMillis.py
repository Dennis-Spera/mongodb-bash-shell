#!/usr/bin/env python3

"""

 File: avgMillis.py
 Author: Dennis Spera
 Date: 2024-06-24
 Description: count of commands.
 Description: 
  1.) calculate average durationMillis from mongod.log(s) for the given time period.

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

millis = list()
totMillis = 0
countMillis = 0
avgMillis = 0.0

for json in jsonFile:
    if json['c'] == 'COMMAND':
       try:
        millis.append({'json':j.dumps(json),'milli':json['attr']['durationMillis']})
        totMillis += int(json['attr']['durationMillis'])    
        countMillis +=1
       except:
        pass
       
if countMillis > 0:
   avgMillis = round((totMillis/countMillis),2)
   print ('The average time for commands: ',  avgMillis,'ms')

else:
   print ('No commands found with a durationMillis specified')   

