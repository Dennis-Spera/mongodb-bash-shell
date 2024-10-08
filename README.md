## The package is designed to interact with the other commands found documented here. Concidering this is meant to be used as a pipeline, these pipelines can also interact with other linux command when used in the correct context. Some of these commands are designed to interact with streaming json similiar to client-server they have to be in the right format to be used together. These commands would be bytesRead, collScans, docsExamined, jsonFetcher, keysExamined, millis and ns.   

**Setup**

**test in virtual environment**
**---------------------------**


```bash
# Create the virtual environment
pip install virtualenv
mkdir mshell
cd mshell
python3 -m venv mongo-shell
cd mongo-shell
source bin/activate
```

```bash
# clone respository
git clone https://github.com/Dennis-Spera/mongodb-bash-shell.git
cd mongodb-bash-shell
export MSHELL=$PWD
bash mkSetup.sh
pip install -r requirements.txt
```
**add to your normal environment**
**------------------------------**

```bash
source bin/deactivate
rm -rf mshell
git clone https://github.com/Dennis-Spera/mongodb-bash-shell.git
cd mongodb-bash-shell
add to end of your .zprofile
export MSHELL=full path of mongodb-bash-shell directory
add all the functions contained in mkSetup.sh
pip install -r requirements.txt
source $HOME/.zprofile
```

**Inventory of files**

 1. **appName.py** - a list of all the apps for the specified time period.
 2. **avgMillis.py** - the average of milliseconds for all commands during a given time period.
 3. **bytesRead.py** - sort json by bytes read
 4. **code.sh** - called by vscode.py to call vscode
 5. **collScans.py** - list json that is a collection scan
 6. **convertLogs.py** - this is a cloned copy of generate_mplot_logs.py I modified to enable pipelineing
 7. **countCommands.py** - give a count of different commands for a given time period - (beta)
 8. **docsExamined.py** - sort json by docsExamined
 9. **drivers.py** - aggegate counts for all drivers used during a time period
10. **formatOne.py** - format the piped json displaying releavant data stripping off unnecessary data 
11. **jsonFetcher.py** - returns all the json that fall between a begin date and end date
12. **keysExamined.py** - sort json by keysExamined
13. **millis.py** - sort json by milliseconds
14. **mkConsh.py** - makes shell script used to extract connection info
15. **mkSetup.sh** - makes the environment for appending to your profile
16. **mplot.py** - execute `mplotqueries.py` based on piped input
17. **mplotqueries.py** - legacy script cloned to this repository for convenience
18. **nsIndexes.py** - list the indexes used by namespace with a count
19. **ns.py** - sort json by namespace
20. **phead.py** - the installed head command sends a `SIGTERM` to cat command, this is the python version
21. **queryHash.py** - list query shapes (query shapes) and counts
22. **README.md** - this file
23. **vscode.py** - pipe standard out to a vscode tab
24. **loadvs-pkg.sh** - script to load all files into vscode tabs
25. **test.sh** - script with 3 tests using jq to validate




**Example 1 - count the number of json entries for the date range**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to the linux `wc -l` command
 calculating the count of records for the specified dateframe.

```bash
% cat mongodb.log | jsonFetcher -b 20200601000000 -e 20250630000000 | wc -l

```
**Example 2 - count the number of of each of the common commands**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to countCommands which calculates
 the count for different commands based on the timeframe and cast to a vscode tab.

```bash
% cat mongodb.log |  jsonFetcher -b 20200601000000 -e 20250630000000 | countCommands | vscode

```

**Example 3 - order the json by highest duration milliseconds and format the output and cast to a vscode tab**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to millis command which will
 sort based on durationMillis and pipe that to formatOne which will present the json in a more readable format

```bash
% cat mongodb.log |  jsonFetcher -b 20200601000000 -e 20250630000000 | millis | formatOne | vscode

```

**Example 5 - compute the average milliseconds for the time period**

logic: Compile the average durationMillis for a given  time period and cast the output to a vscode tab

```bash
% cat mongodb.log |  jsonFetcher -b 20200601000000 -e 20250630000000 | avgMillis | vscode

```

**Example 6 - get the json with the 2 highest bytes read, format the output and send to a vscode tab**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to bytesRead command which will
 sort based on bytesRead and pipe that to phead which will grab the 2 highest queries byteRead then pipe that to formatOne 
 which will present the json in a more readable format and then pipe that to a vscode tab instead of stdout

```bash
% cat mongodb.log |  jsonFetcher -b 20200601000000 -e 20250630000000 | bytesRead | phead -r 2 | formatOne | vscode

```

**Example 7 - get the app names and count for the given time frame and cast to vscode**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to appName to get all the appNames
 with their count.

```bash
% cat mongodb.log |  jsonFetcher -b 20200601000000 -e 20250630000000 | appName | vscode

```

**Example 8 - order the json by docExamined return the top 3 and format the text and send to a vscode tab**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to docsExamined this will return
 the full json ordered by docsExamined, then takes the top 3 because of phead, pipe that to formatOne to increase readability
 and then pipe it to a vscode tab.
 
```bash
% cat mongodb.log | jsonFetcher -b 20200601000000 -e 20250630000000 | docsExamined | phead -r 3 | formatOne | vscode

```

**Example 9 - get connection stats using legacy code**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified date time frame and then pass that to convertLogs to convert
 logs 5.+ to 4.4 and before which will pipe that to a modified version of generate_mplot_logs.py that permits input from 
 stdin/pipe, by generating a bash script, calling it and piping to vscode

```bash
% cat mongodb.log |  jsonFetcher -b 20200601000000 -e 20250630000000 | convertLogs | mkConsh; bash connStats.sh | vscode

```

**Example 10 - piping into mplotqueries.py**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified time frame and then pass that to convertLogs to convert
 logs 5.+ to 4.4 (generate_mplot_logs.py was modified to allow piped input) and will pipe that into mplotqueries.py using a bash script

```bash
% cat mongodb.log | jsonFetcher -b 20240101000000 -e 20250101000000 |  convertLogs | mplot
```

**Example 11 - piping into multiple filters collScans, millis -- collections scans sorted by millisreconds high to low**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified time frame and then pass that to collScans to millis to phead 
 this will yield the top 3 collections scan by duration in milliSeconds

```bash
% cat mongodb.log | jsonFetcher -b 20220601000000 -e 20250630000000 | collScans | millis | phead -r 3 | formatOne | vscode

```
**Example 12 - list drivers and counts**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified time frame and then pipe that to drivers and pipe to vscode

```bash
% cat mongodb.log | jsonFetcher -b 20240101000000 -e 20250101000000 | drivers | vscode

```

**Example 13 - sorting by namespace**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified time frame and then pipe that to millis to sort to milliseconds
 then pipe to phead to select the top 10 in milliseconds and then pipe that into ns to sort by namespace, format the output
 and then cast it to a vscode tab.

```bash
% cat mongodb.log | jsonFetcher -b 20240101000000 -e 20250101000000 | millis | phead -r 10 | ns | formatOne | vscode
```

**Example 14 - extract indexes with counts**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified time frame and then pipe that to indexes to get indexes by 
 namespace and count and then cast it to a vscode tab.

```bash
% cat mongodb.log | jsonFetcher -b 20240101000000 -e 20250101000000 | indexes | vscode

```

**Addendum**

You may need to add the following to invoke vscode and load a file

code () { VSCODE_CWD="$PWD" open -n -b "com.microsoft.VSCode" --args $* ;}
