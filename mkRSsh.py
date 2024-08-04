#!/usr/bin/env python3

"""

 File: mkRSsh.py
 Author: Dennis Spera
 Date: 2024-06-24
 Description: 
  1.) generate script that calls mloginfo.py.


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
  file = open("rsInfo.sh", "w")
  file.write(os.environ['PYTHON_BIN']+' '+os.environ['MSHELL']+'/'+'mloginfo.py --rsinfo '+temp.name)
  file.close()

except:
 sys.stderr.write('mloginfo.py could not be executed, check mplotqueries setup')

temp.close() 