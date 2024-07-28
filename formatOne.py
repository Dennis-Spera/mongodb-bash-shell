#!/usr/bin/env python3

"""

 File: formatOne.py
 Author: Dennis Spera
 Date: 2024-06-24
 Description: 
  1.) concise format(1) of mongod.log(s) on stdin.

 Change Log:
  1. 2024-06-24 - Initial
  2. 2024-07-13 - Add additional error checking and global help fucntion

 Testing: 
  1. Not defined
"""

import json, sys
from collections import Counter
import json as j

jsonFile = list()

for line in sys.stdin:
  try:
    jsonFile.append( j.loads(line))
  except:
    pass
  
sys.stdin.close()

formatted = list()
for json in jsonFile:
    if json['c'] == 'COMMAND':

        try: print("{:<20} {:<1} {:>0}".format('Submission Time ', '=', json['t']['$date']))
        except: pass
        try: print("{:<20} {:<1} {:>0}".format('command ', '=', str(json['attr']['command'])))
        except: pass

        print("\n")

        try: print("{:<20} {:<1} {:>0}".format('ns|name space ', '=', str(json['attr']['ns'])))
        except: pass
        try: print("{:<20} {:<1} {:>0}".format('planSummary ', '=', json['attr']['planSummary']))
        except: pass
        try: print("{:<20} {:<1} {:>0}".format('keysExamined ', '=', json['attr']['keysExamined']))
        except: pass
        try: print("{:<20} {:<1} {:>0}".format('docsExamined ', '=', json['attr']['docsExamined']))
        except: pass
        try: print("{:<20} {:<1} {:>0}".format('queryHash ', '=', json['attr']['queryHash']))
        except: pass
        try: print("{:<20} {:<1} {:>0}".format('numYields ', '=', json['attr']['numYields']))
        except: pass
        try: print("{:<20} {:<1} {:>0}".format('nreturned  ', '=', json['attr']['nreturned']))
        except: pass 
        try: print("{:<20} {:<1} {:>0}".format('durationMillis ', '=', json['attr']['durationMillis']))
        except: pass 
        try: print("{:<20} {:<1} {:>0}".format('remote ', '=', json['attr']['remote']))
        except: pass 
        try: print("{:<20} {:<1} {:>0}".format('bytesRead ', '=', json['attr']['storage']['data']['bytesRead']))
        except: pass 

        print("-----------------------------------------------------------------------------------------------------\n")

       
