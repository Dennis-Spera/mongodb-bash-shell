#!/usr/bin/env python3

"""

 File: lv.py
 Author: Dennis Spera
 Date: 2024-06-24
 Description: 
  1.) write stdin to a file to be read in by lv.

 Change Log:
  1. 2024-06-24 - Initial

 Testing: 
  1. Not defined

"""

import tempfile
import sys, os
import tempfile

tempfile.tempdir = "/tmp"
temp = tempfile.TemporaryFile(delete=False)

for line in sys.stdin:
    temp.write(line.encode())
       
sys.stdin.close()
temp.close()
try:
 os.system('lv '+temp.name)
 
except Exception as e:
 sys.stderr.write('lv could not be executed, check lv setup')
 sys.stderr.write('---------------------------------------------------------------------------------')
 sys.stderr.write(e)