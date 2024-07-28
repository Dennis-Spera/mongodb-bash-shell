#!/usr/bin/env python3

"""

 File: mplot.py
 Author: Dennis Spera
 Date: 2024-06-24
 Description: 
  1.) write stdin to a file to be read in by mplotqueries.py.


 Change Log:
  1. 2024-06-24 - Initial

 Testing: 
  1. Not defined

"""

import tempfile
import sys, os
import tempfile

tempfile.tempdir = "/tmp"
temp = tempfile.NamedTemporaryFile('w',delete=False)

for line in sys.stdin:
    temp.write(line)
       
sys.stdin.close()
temp.close()
try:
 os.system(os.environ['PYTHON_BIN']+' mplotqueries.py<'+temp.name)
 
except Exception as e:
 sys.stderr.write(e)
 sys.stderr.write('mplotqueries could not be executed, check mplotqueries setup')