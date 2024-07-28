#!/usr/bin/env python3

"""

 File: vscode.py
 Author: Dennis Spera
 Date: 2024-06-24
 Description: 
  1.)  Description: load stdin directly into vscode tab.

 Change Log:
  1. 2024-06-24 - Initial

 Testing: 
  1. notify when there is no stdin
"""

import tempfile
import sys, os

tempfile.tempdir = "/tmp"
temp = tempfile.NamedTemporaryFile('w',delete=False)

for line in sys.stdin:
    temp.write(line)

sys.stdin.close()
temp.close()

try:
 os.system('code'+' '+temp.name)
except:
 sys.stderr.write('code could not be executed, check vscode setup')