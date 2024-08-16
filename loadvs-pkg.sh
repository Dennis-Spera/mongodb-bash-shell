#!/bin/bash

if ["$HOSTTYPE" == "arm64"] 2> /dev/null; then

      export directory=$PWD
      code () {
            VSCODE_CWD="$PWD" open -n -b "com.microsoft.VSCode" --args $*
      } 
     
else
      export directory=$PWD
fi

code -r $directory --args file loadvs-pkg.sh appName.py docsExamined.py mkRSsh.py phead.py\
                          avgMillis.py drivers.py mkSetup.sh queryHash.py bytesRead.py formatOne.py\
                          mloginfo.py README.md code.sh jsonFetcher.py mplot.py requirements.txt\
                          collScans.py keysExamined.py mplotqueries.py vscode.py convertLogs.py\
                          millis.py nsIndexes.py countCommands.py mkConsh.py ns.py 2> /dev/null