#!/usr/bin/env python3

"""

 File: countCommands.py
 Author: Dennis Spera
 Date: 2024-06-24
 Description: count of commands.
 Description: 
  1.) count the number of different commands for the specified times period.

 Change Log:
  1. 2024-06-24 - Initial 

 Testing: 
  1. Not defined
"""

import json, sys
import json as j
import re as regex

jsonFile = list()

for line in sys.stdin:
    jsonFile.append( j.loads(line))
sys.stdin.close()

countFind = 0
countDelete = 0
countInsert = 0
countUpsert = 0
countUpdate = 0 
countGetmore = 0

'''
 try/except to bypass runtime error when there is no command attribute present
'''
for json in jsonFile:


    if json['c'] == 'COMMAND':
       try:
        if regex.search("\'find\'", str(json['attr']['command']), regex.IGNORECASE) or regex.search("\'q\'", str(json['attr']['command']), regex.IGNORECASE):                    
            countFind +=1
       except: pass
       try:     
        if regex.search("\'delete\'", str(json['attr']['command']), regex.IGNORECASE) or regex.search("\'d\'", str(json['attr']['command']), regex.IGNORECASE):                    
            countDelete +=1
       except: pass
       try:     
        if regex.search("\'insert\'", str(json['attr']['command']), regex.IGNORECASE) or regex.search("\'i\'", str(json['attr']['command']), regex.IGNORECASE):                    
            countInsert +=1
       except: pass
       try:     
        if regex.search("\'upsert\'", str(json['attr']['command']), regex.IGNORECASE):                    
            countUpsert +=1
       except: pass
       try:     
        if regex.search("\'update\'", str(json['attr']['command']), regex.IGNORECASE) or regex.search("\'u\'", str(json['attr']['command']), regex.IGNORECASE):                    
            countUpdate +=1            
       except: pass
       try:
        if regex.search("\'getmore\'", str(json['attr']['command']), regex.IGNORECASE):                    
            countGetmore +=1            
       except: pass 


# print totals
print("{:<20} {:<1} {:>0}".format('Count of find commands    ', '=', countFind))
print("{:<20} {:<1} {:>0}".format('Count of delete commands  ', '=', countDelete))
print("{:<20} {:<1} {:>0}".format('Count of insert commands  ', '=', countInsert))
print("{:<20} {:<1} {:>0}".format('Count of upsert commands  ', '=', countUpsert))
print("{:<20} {:<1} {:>0}".format('Count of update commands  ', '=', countUpdate))
print("{:<20} {:<1} {:>0}".format('Count of getmore commands ', '=', countGetmore))
