#!/usr/bin/env python3

"""

 File: queryHash.py
 Author: Dennis Spera
 Date: 2024-06-24
 Description: 
  1.) Aggregate the count of query shapes.

 Change Log:
  1. 2024-06-24 - Initial 

 Testing: 
  1. Not defined
"""

from collections import Counter, OrderedDict
import sys, re
import json as j

jsonFile = list()

for line in sys.stdin:
    jsonFile.append( j.loads(line))
sys.stdin.close()

queryHash = list()
for json in jsonFile:
    if json['c'] == 'COMMAND':
      try:
        #queryHash.append({'json':j.dumps(json),'queryHash':json['attr']['queryHash']})
        queryHash.append(json['attr']['queryHash'])        
      except:
       pass
       
#try:       
# sorted_list = sorted(queryHash, key=lambda x: x['queryHash'], reverse=True)
#
# for element in sorted_list:
#     print(element['json']) 
#except:
#   sys.stderr.write('No useable data found'+"\n")



queryHashTotals = dict(Counter(queryHash))
sortedByKey = OrderedDict(sorted(queryHashTotals.items()))
sortedByValue = {k: v for k, v in sorted(queryHashTotals.items(), key=lambda item: item[1], reverse=True)}

print("{:>10}   {:<10}".format('Count', 'queryHash'))
print("{:>10}   {:<10}".format('-----', '----------------------'))

for k,v in sortedByValue.items():
    print("{:>10}   {:<10}".format(v, k))    