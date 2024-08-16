#!/usr/bin/bash

# setup for shell
export MSHELL=$PWD


jsonFetcher () {
    python3 $MSHELL/jsonFetcher.py $*
}
export -f jsonFetcher

countCommands () {
    python3 $MSHELL/countCommands.py $*
}
export -f countCommands

millis () {
    python3 $MSHELL/millis.py $*
}
export -f millis

formatOne () {
    python3 $MSHELL/formatOne.py $*
}
export -f formatOne

vscode () {
    python3 $MSHELL/vscode.py $*
}   
export -f vscode

avgMillis () {
    python3 $MSHELL/avgMillis.py $*
}
export -f avgMillis

bytesRead () {
    python3 $MSHELL/bytesRead.py $*
}   
export -f bytesRead

phead () {
    python3 $MSHELL/phead.py $*
}
export -f phead

appName () {
    python3 $MSHELL/appName.py $*
}
export -f appName

docsExamined () {
    python3 $MSHELL/docsExamined.py $*
}       
export -f docsExamined

keysExamined () {
    python3 $MSHELL/keysExamined.py $*
}   
export -f keysExamined

convertLogs () {
    python3 $MSHELL/convertLogs.py $*
}   
export -f convertLogs

mkConsh () {
    python3 $MSHELL/mkConsh.py $*
}   
export -f mkConsh

mkRSsh () {
    python3 $MSHELL/mkRSsh.py $*
}   
export -f mkRSsh

mplot () {
    python3 $MSHELL/mplot.py $*
}   
export -f mplot

collScans () {
    python3 $MSHELL/collScans.py $*
}   
export -f collScans

drivers () {
    python3 $MSHELL/drivers.py $*
}
export -f drivers

ns () {
    python3 $MSHELL/ns.py $*
}
export -f ns

indexes () {
    python3 $MSHELL/nsIndexes.py $*
}
export -f indexes

queryHash () {
    python3 $MSHELL/queryHash.py $*
}
export -f queryHash