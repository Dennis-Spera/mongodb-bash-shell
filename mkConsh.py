#!/usr/bin/env python3

"""
 File: mkConsh.py
 Author: Dennis Spera
 Date: 2024-06-24
 Description: 
  1.) output the command string for processing connection stats

 Change Log:
  1. 2024-06-24 - Initial 

 Testing: 
  1. Not defined
"""

import tempfile
import sys, os

tempfile.tempdir = "/tmp"
temp = tempfile.NamedTemporaryFile('w',delete=False)

for line in sys.stdin:
    temp.write(line)
       
sys.stdin.close()

try:
  file = open("connStats.sh", "w")
  file.write(os.environ['PYTHON_BIN']+' '+os.environ['MSHELL']+'/'+'mloginfo.py --connstats '+temp.name)
  file.close()

except:
 sys.stderr.write('mloginfo.py could not be executed, check mplotqueries setup')

temp.close() 