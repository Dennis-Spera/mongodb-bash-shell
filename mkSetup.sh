#!/usr/bin/bash

# setup for shell

bash <<EOF
echo "
export MSHELL=$PWD
export PATH=$PATH:$MSHELL
export PYTHON_BIN=`which python3`
alias jsonFetcher='$PYTHON_BIN $MSHELL/jsonFetcher.py'
alias countCommands='$PYTHON_BIN $MSHELL/countCommands.py'
alias millis='$PYTHON_BIN $MSHELL/millis.py'
alias formatOne='$PYTHON_BIN $MSHELL/formatOne.py'
alias vscode='$PYTHON_BIN $MSHELL/vscode.py'
alias avgMillis='$PYTHON_BIN $MSHELL/avgMillis.py'
alias bytesRead='$PYTHON_BIN $MSHELL/bytesRead.py'
alias phead='$PYTHON_BIN $MSHELL/phead.py'
alias appName='$PYTHON_BIN $MSHELL/appName.py'
alias docsExamined='$PYTHON_BIN $MSHELL/docsExamined.py'
alias keysExamined='$PYTHON_BIN $MSHELL/keysExamined.py'
alias convertLogs='$PYTHON_BIN $MSHELL/convertLogs'
alias mkConsh='$PYTHON_BIN $MSHELL/mkConsh.py'
alias mkRSsh='$PYTHON_BIN $MSHELL/mkRSsh.py'
alias mplot='$PYTHON_BIN $MSHELL/mplot.py'
alias collScans='$PYTHON_BIN $MSHELL/collScans.py'
alias drivers='$PYTHON_BIN $MSHELL/drivers.py'
alias lvv='$PYTHON_BIN $MSHELL/lv.py'
alias ns='$PYTHON_BIN $MSHELL/ns.py'
alias indexes='$PYTHON_BIN $MSHELL/nsIndexes.py'
alias queryHash='$PYTHON_BIN $MSHELL/queryHash.py'
"
EOF

echo
echo  'append the above to the end of your profile, then'
echo  'ubuntu: . $HOME/.profile'
echo  'mac: . $HOME/.zprofile'
