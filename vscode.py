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

import tempfile, sys, subprocess

tempfile.tempdir = "/tmp"
temp = tempfile.NamedTemporaryFile('w',delete=False)

for line in sys.stdin:
    temp.write(line)

sys.stdin.close()
temp.close()

try:
  subprocess.run(["code", temp.name])
except:
  subprocess.run(["bash", "code.sh", temp.name])  
