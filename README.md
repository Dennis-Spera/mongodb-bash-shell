## The enclosed commands are designed to closely integrate with other shell commands. The logic being what if the linux distribution had these commands built into it.

**Setup**

install locally
----------------------


```bash
# Create the virtual environment
pip install virtualenv
mkdir mshell
cd mshell
python3 -m venv mongo-shell
source bin/activate

# clone respository
git clone https://github.com/Dennis-Spera/mongodb-bash-shell.git
cd mongodb-bash-shell
bash mkSetup.sh
```

**Virtual environment**

**Add to your working environment**

copy contents to the end of your profile
restart shell

**Inventory of scripts**

scripts:

 1. **appName.py** - a list of all the apps for the specified time period.
 2. **avgMillis.py** - the average of milliseconds for all commands during a given time period.
 3. **bytesRead.py** - sort json by bytes read
 4. **code.sh** - called by vscode.py to call vscode
 5. **collScans.py** - list json that is a collection scan
 6. **convertLogs.py** - this is a cloned copy of generate_mplot_logs.py modified to enable pipelineing
 7. **countCommands.py** - give a count of different commands for a given time period - (beta)
 8. **docsExamined.py** - sort json by docsExamined
 9. **drivers.py** - aggegate counts for all drivers used during a time period
10. **formatOne.py** - format the piped json displaying releavant data stripping off unnecessary data 
11. **jsonFetcher.py** - returns all the json that fall between a begin date and end date
12. **keysExamined.py** - sort json by keysExamined
13. **lv.py** - optimize the time it takes lv to load
14. **millis.py** - sort json by milliseconds
15. **mkConsh.py** - makes shell script used to extract connection info
16. **mkRSsh.py** - makes shell script used to extract replication info
17. **mkSetup.sh** - makes the environment for appending to your profile
18. **mplot.py** - execute `mplotqueries.py` based on piped input
19. **nsIndexes.py** - list the indexes used by namespace with a count
20. **ns.py** - sort json by namespace
21. **phead.py** - the installed head command sends a `SIGTERM` to cat command, this is the python version
22. **queryHash.py** - list query shapes (query shapes) and counts
23. **README.md** - this file
24. **vscode.py** - pipe standard out to a vscode tab



**Example 1**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to the linux `wc -l` command
 calculating the count of records for the specified dateframe.

```bash
% cat mongodb.log | jsonFetcher -b 20200601000000 -e 20250630000000 | wc -l

395596
```
**Example 2**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to countCommands which calculates
 the count for different commands based on the timeframe.

```bash
% cat mongodb.log |  jsonFetcher -b 20200601000000 -e 20250630000000 | countCommands | vscode

```

**Example 3**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to millis command which will
 sort based on durationMillis and pipe that to formatOne which will present the json in a more readable format

```bash
% cat mongodb.log |  jsonFetcher -b 20200601000000 -e 20250630000000 | millis | formatOne | vscode

```

**Example 5**

logic: Compile the average durationMillis for a given  time period and cast the output to a vscode tab

```bash
% cat mongodb.log |  jsonFetcher -b 20200601000000 -e 20250630000000 | avgMillis | vscode

```

**Example 6**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to bytesRead command which will
 sort based on bytesRead and pipe that to phead which will grab the 2 highest queries byteRead then pipe that to formatOne 
 which will present the json in a more readable format and then pipe that to a vscode tab instead of stdout

```bash
% cat mongodb.log |  jsonFetcher -b 20200601000000 -e 20250630000000 | bytesRead | phead -r 2 | formatOne | vscode

```

**Example 7**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to appName to get all the appNames
 with their count.

```bash
% cat mongodb.log |  jsonFetcher -b 20200601000000 -e 20250630000000 | appName | vscode

```

**Example 8**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to docsExamined this will return
 the full json ordered by docsExamined, then takes the top 3 because of phead, pipe that to formatOne to increase readability
 and then pipe it to a vscode tab.
 
```bash
% cat mongodb.log.2024-06-11T02-49-10 | jsonFetcher -b 20240601000000 -e 20240630000000 | docsExamined | phead -r 3 | formatOne | vscode

```

**Example 9**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified date time frame and then pass that to convertLogs to convert
 logs 5.+ to 4.4 and before which will pipe that to a modified version of generate_mplot_logs.py that permits input from 
 stdin/pipe, by generating a bash script, calling it and piping to vscode

```bash
% cat mongodb.log| jsonFetcher -b 20240101000000 -e 20250101000000 |

     source: /tmp/tmp4se7_cx3
       host: atlas-vvn46p-shard-00-00.lxayk.mongodb.net:27017
      start: 2024 Jun 10 02:49:00.159
        end: 2024 Jun 11 02:48:37.369
date format: iso8601-local
   timezone: UTC
     length: 392357
     binary: unknown
    version: >= 3.0 (iso8601 format, level, component)
    storage: unknown

CONNECTIONS
     total opened: 80399
     total closed: 80399
    no unique IPs: 12
socket exceptions: 0
overall average connection duration(s): 612.2208498271283
overall minimum connection duration(s): 0
overall maximum connection duration(s): 20200

10.20.192.11     opened: 20960     closed: 20960    dur-avg(s): 658      dur-min(s): 600      dur-max(s): 660     
10.20.207.199    opened: 19650     closed: 19650    dur-avg(s): 659      dur-min(s): 658      dur-max(s): 660     
10.20.196.4      opened: 9170      closed: 9170     dur-avg(s): 658      dur-min(s): 600      dur-max(s): 660     
10.20.202.78     opened: 7860      closed: 7860     dur-avg(s): 659      dur-min(s): 658      dur-max(s): 660     
10.20.202.248    opened: 7800      closed: 7800     dur-avg(s): 658      dur-min(s): 658      dur-max(s): 660     
192.168.240.198  opened: 5736      closed: 5736     dur-avg(s): 0        dur-min(s): 0        dur-max(s): 0       
10.20.203.71     opened: 5240      closed: 5240     dur-avg(s): 658      dur-min(s): 600      dur-max(s): 660     
10.20.209.155    opened: 3930      closed: 3930     dur-avg(s): 659      dur-min(s): 659      dur-max(s): 660     
192.168.241.141  opened: 35        closed: 35       dur-avg(s): 20       dur-min(s): 0        dur-max(s): 61      
192.168.242.223  opened: 10        closed: 10       dur-avg(s): 9262     dur-min(s): 108      dur-max(s): 20200   
3.122.44.223     opened: 5         closed: 5        dur-avg(s): 0        dur-min(s): 0        dur-max(s): 1       
3.127.55.6       opened: 3         closed: 3        dur-avg(s): 0        dur-min(s): 0        dur-max(s): 1       

```

**Example 10**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified time frame and then pass that to convertLogs to convert
 logs 5.+ to 4.4 (generate_mplot_logs.py was modified to allow piped input) and will pipe that into mloginfo.py using a bash script and piping to vscode

```bash
% cat mongodb.log.2024-06-11T02-49-10 | jsonFetcher -b 20240101000000 -e 20250101000000 |  convertLogs | mkRSsh; bash rsInfo.sh | vscode

     source: /tmp/tmpvq9qb9fx
       host: atlas-vvn46p-shard-00-00.lxayk.mongodb.net:27017
      start: 2024 Jun 10 02:49:00.159
        end: 2024 Jun 11 02:48:37.369
date format: iso8601-local
   timezone: UTC
     length: 392357
     binary: unknown
    version: >= 3.0 (iso8601 format, level, component)
    storage: unknown

RSINFO
  no rs info changes found
```

**Example 11 - piping into mplotqueries.py**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified time frame and then pass that to convertLogs to convert
 logs 5.+ to 4.4 (generate_mplot_logs.py was modified to allow piped input) and will pipe that into mplotqueries.py using a bash script

```bash
% cat mongodb.log.2024-06-11T02-49-10 | jsonFetcher -b 20240101000000 -e 20250101000000 |  convertLogs | mplot
```

**Example 12 - piping into multiple filters collScans, millis -- collections scans sorted by millisreconds high to low**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified time frame and then pass that to collScans to millis to phead 
 this will yield the top 3 collections scan by duration in milliSeconds

```bash
% cat *mongodb.log* | jsonFetcher -b 20220601000000 -e 20250630000000 | collScans | millis | phead -r 3 | formatOne | vscode


Submission Time      = 2024-05-10T06:46:43.191+00:00
command              = {'find': 'vw_ent_store_adaptablity_rpt', 'filter': {}, 'limit': 0, 'projection': {'_id': 1, 'enterprise_name': 1, 'Today': 1, 'Yesterday': 1, 'Last7Days': 1, 'Last30Days': 1, 'enterprise_id': 1, 'store_id': 1, 'store_name': 1, 'is_default_store': 1}, 'skip': 0, 'lsid': {'id': {'$uuid': '80ab7df6-ff1d-4a22-9a84-9dfdfb9f123d'}}, '$clusterTime': {'clusterTime': {'$timestamp': {'t': 1715323500, 'i': 4}}, 'signature': {'hash': {'$binary': {'base64': 'pZou1Yfm5hbXfbGF4+vyWM0UksM=', 'subType': '0'}}, 'keyId': 7314772094741381122}}, '$db': 'unify-prod', '$readPreference': {'mode': 'primary'}}


ns|name space        = unify-prod.vw_ent_store_adaptablity_rpt
planSummary          = COLLSCAN
keysExamined         = 50446
docsExamined         = 121296359
queryHash            = 55370F70
numYields            = 116233
nreturned            = 101
durationMillis       = 101623
remote               = 192.168.240.197:53139
bytesRead            = 54682308
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-05-10T06:56:43.723+00:00
command              = {'find': 'vw_ent_def_store_adaptablity_rpt', 'filter': {}, 'limit': 0, 'projection': {'Yesterday': 1, 'Last7Days': 1, 'Last30Days': 1, 'enterprise_id': 1, 'store_name': 1, 'is_default_store': 1, 'Today': 1, '_id': 1, 'enterprise_name': 1, 'store_id': 1}, 'skip': 0, 'lsid': {'id': {'$uuid': '04cf6491-26e6-48b8-bf83-1286792997a0'}}, '$clusterTime': {'clusterTime': {'$timestamp': {'t': 1715324100, 'i': 5}}, 'signature': {'hash': {'$binary': {'base64': 'ycLP46Tdlo+5/uTSPmPpACgJpU0=', 'subType': '0'}}, 'keyId': 7314772094741381122}}, '$db': 'unify-prod', '$readPreference': {'mode': 'primary'}}


ns|name space        = unify-prod.vw_ent_def_store_adaptablity_rpt
planSummary          = COLLSCAN
keysExamined         = 50446
docsExamined         = 121227503
queryHash            = 55370F70
numYields            = 116167
nreturned            = 101
durationMillis       = 101379
remote               = 192.168.242.52:25155
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-05-10T06:16:53.772+00:00
command              = {'aggregate': 'audit_checks', 'pipeline': [{'$lookup': {'from': 'check_sums_tmp_20240510_061526_dGlGKT', 'let': {'check_col_name': '$col_name', 'check_col_id': '$col_id', 'check_cur_check_sum': '$cur_hash_val'}, 'pipeline': [{'$match': {'$expr': {'$and': [{'$eq': ['$col_name', '$$check_col_name']}, {'$eq': ['$col_id', '$$check_col_id']}, {'$ne': ['$cur_check_sum', '$$check_cur_check_sum']}]}}}, {'$project': {'col_name': 0, 'check_col_id': 0}}], 'as': 'tmp_check_sums'}}, {'$unwind': {'path': '$tmp_check_sums', 'preserveNullAndEmptyArrays': True}}, {'$project': {'_id': 1, 'col_id': 1, 'col_name': 1, 'created_at': 1, 'created_by': 1, 'cur_hash_val': 1, 'is_active': 1, 'prev_hash_val': 1, 'updated_at': 1, 'updated_by': 1, 'tmp_chk_sum': '$tmp_check_sums.cur_check_sum'}}, {'$match': {'$and': [{'tmp_chk_sum': {'$exists': True}}, {'tmp_chk_sum': {'$ne': ''}}]}}, {'$project': {'_id': 1, 'col_id': 1, 'col_name': 1, 'created_at': 1, 'created_by': 1, 'cur_hash_val': '$tmp_chk_sum', 'is_active': 1, 'prev_hash_val': '$cur_hash_val', 'updated_at': '$$NOW', 'updated_by': 'daily_process'}}, {'$merge': {'into': 'audit_checks', 'on': '_id', 'whenMatched': 'replace'}}], 'cursor': {}, 'lsid': {'id': {'$uuid': 'beb3b4b6-9b37-474c-b570-13910a4f9140'}}, '$clusterTime': {'clusterTime': {'$timestamp': {'t': 1715321749, 'i': 1}}, 'signature': {'hash': {'$binary': {'base64': '/sd7+D1464bNfFnz9L8zT74p5Yk=', 'subType': '0'}}, 'keyId': 7314772094741381122}}, '$db': 'unify-prod'}


ns|name space        = unify-prod.audit_checks
planSummary          = COLLSCAN
keysExamined         = 379276
docsExamined         = 758555
queryHash            = E852E4BF
numYields            = 396
nreturned            = 0
durationMillis       = 62453
remote               = 192.168.240.197:23892
bytesRead            = 107417041
-----------------------------------------------------------------------------------------------------
```
**Example 13 - piping into multiple filters collScans, millis -- collections scans sorted by millisreconds high to low**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified time frame and then pipe that to drivers and pipe to vscode

```bash
% cat *mongodb.log* | jsonFetcher -b 20240101000000 -e 20250101000000 | drivers | vscode

     Count   Driver    
     -----   ----------------------
    186735   mongo-java-driver|reactive-streams <version> 4.10.2
     58165   mongo-go-driver <version> v1.12.0-cloud
     33798   mongo-csharp-driver <version> 2.19.1.0
     21720   mongo-go-driver <version> v1.11.3
     19218   mongo-java-driver|sync|spring-boot <version> 4.4.2
      3803   mongo-go-driver <version> v1.12.1
       407   mongo-csharp-driver <version> 2.21.0.0
       116   nodejs <version> 6.7.0
        94   NetworkInterfaceTL <version> 5.0.26
        90   mongo-java-driver|reactive-streams|scala <version> 4.10.2
        85   mongo-java-driver|reactive-streams|spring-boot <version> 4.11.1
        70   mongo-go-driver <version> v1.10.3
        56   nodejs <version> 4.13.0
        50   mongo-java-driver|sync|spring-boot <version> 4.11.1
        45   nodejs|mongosh <version> 4.12.1
        39   nodejs <version> 5.8.1
        34   mongo-java-driver|sync <version> 4.7.2-s3t
        32   MongoDB Internal Client <version> 4.2.6-18-g6cdb6ab
        31   nodejs <version> 5.6.0
        29   NetworkInterfaceTL-MirrorMaestro <version> 6.0.15
        14   nodejs <version> 6.5.0
        14   MongoDB Internal Client <version> 5.0.26
        14   mongo-java-driver|reactive-streams <version> 4.4.2
        13   nodejs <version> 4.3.0
        13   mongo-java-driver|sync <version> 4.4.2
        12   nodejs <version> 6.1.0
        10   mongo-java-driver|legacy <version> 5.1.0
         8   nodejs <version> 6.3.0
         8   nodejs <version> 6.0.0
         4   NetworkInterfaceTL <version> 4.2.6-18-g6cdb6ab
         3   mongo-go-driver <version> v1.11.7
         3   MongoDB Internal Client <version> 6.0.16
         2   NetworkInterfaceTL-ReplNetwork <version> 6.0.16
         2   NetworkInterfaceTL-ReplicaSetMonitor-TaskExecutor <version> 6.0.16
         2   mongo-java-driver|reactive-streams|spring-boot <version> 5.0.1
         1   NetworkInterfaceTL-ReplCoordExternNetwork <version> 6.0.16
         1   NetworkInterfaceTL-MirrorMaestro <version> 6.0.16
```

**Example 14 - piping into lv**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified time frame and then pipe that to the lv program

```bash
% cat *mongodb.log* | jsonFetcher -b 20240101000000 -e 20250101000000 | lvv
```

**Example 15 - sorting by namespace**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified time frame and then pipe that to millis to sort to milliseconds
 then pipe to phead to select the top 10 in milliseconds and then pipe that into ns to sort by namespace, format the output
 and then cast it to a vscode tab.



```bash
% cat mongodb.log | jsonFetcher -b 20240101000000 -e 20250101000000 | millis | phead -r 10 | ns | formatOne | vscode

Submission Time      = 2024-07-11T22:59:43.365+00:00
command              = {'update': 'projectLinks', 'ordered': True, 'writeConcern': {'w': 'majority'}, 'txnNumber': 3, '$db': 'document360-prod', 'lsid': {'id': {'$uuid': 'f037dd6e-d300-44f5-8688-ab5b3b7d582f'}}, '$clusterTime': {'clusterTime': {'$timestamp': {'t': 1720738578, 'i': 5}}, 'signature': {'hash': {'$binary': {'base64': 'Dsh/efMxg0pB0B8F/6iZI/g8JE4=', 'subType': '0'}}, 'keyId': 7356413323094523906}}}


ns|name space        = document360-prod.$cmd
numYields            = 516
durationMillis       = 204474
remote               = 10.0.32.253:37082
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-07-11T22:59:07.099+00:00
command              = {'update': 'projectLinks', 'ordered': True, 'writeConcern': {'w': 'majority'}, 'txnNumber': 3, '$db': 'document360-prod', 'lsid': {'id': {'$uuid': '72d8af67-c9ca-47c1-aa4d-8269f4e17b28'}}, '$clusterTime': {'clusterTime': {'$timestamp': {'t': 1720738581, 'i': 24}}, 'signature': {'hash': {'$binary': {'base64': 'I4ImT5i6Dj/B9hIapMexo+MR50A=', 'subType': '0'}}, 'keyId': 7356413323094523906}}}


ns|name space        = document360-prod.$cmd
numYields            = 395
durationMillis       = 165617
remote               = 10.0.32.253:58722
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-07-11T22:58:55.188+00:00
command              = {'update': 'projectLinks', 'ordered': True, 'writeConcern': {'w': 'majority'}, 'txnNumber': 14, '$db': 'document360-prod', 'lsid': {'id': {'$uuid': '27a12ed4-5486-4765-965c-dc5467c743a2'}}, '$clusterTime': {'clusterTime': {'$timestamp': {'t': 1720738575, 'i': 4}}, 'signature': {'hash': {'$binary': {'base64': 'WmqJozjP2bm8/Fi564bWDFqLGkU=', 'subType': '0'}}, 'keyId': 7356413323094523906}}}


ns|name space        = document360-prod.$cmd
numYields            = 385
durationMillis       = 159284
remote               = 10.0.32.253:58706
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-07-11T22:58:43.926+00:00
command              = {'update': 'projectLinks', 'ordered': True, 'writeConcern': {'w': 'majority'}, 'txnNumber': 2, '$db': 'document360-prod', 'lsid': {'id': {'$uuid': 'bae8a197-0ea0-4d40-9bc1-97bd76b4df66'}}, '$clusterTime': {'clusterTime': {'$timestamp': {'t': 1720738563, 'i': 7}}, 'signature': {'hash': {'$binary': {'base64': 'VFDTXzrrtkp1TMtYwx2mPLL2gXw=', 'subType': '0'}}, 'keyId': 7356413323094523906}}}


ns|name space        = document360-prod.$cmd
numYields            = 383
durationMillis       = 159282
remote               = 10.0.32.253:37160
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-07-11T22:59:43.727+00:00
command              = {'update': 'projectLinks', 'ordered': True, 'writeConcern': {'w': 'majority'}, 'txnNumber': 3, '$db': 'document360-prod', 'lsid': {'id': {'$uuid': '27025059-87c8-46aa-8df7-3b7dabc7195d'}}, '$clusterTime': {'clusterTime': {'$timestamp': {'t': 1720738624, 'i': 8}}, 'signature': {'hash': {'$binary': {'base64': '1XEM2NkuuFQNlxv6IuiCdjRqoWg=', 'subType': '0'}}, 'keyId': 7356413323094523906}}}


ns|name space        = document360-prod.$cmd
numYields            = 401
durationMillis       = 158489
remote               = 10.0.32.253:43536
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-07-11T22:59:41.902+00:00
command              = {'update': 'projectLinks', 'ordered': True, 'writeConcern': {'w': 'majority'}, 'txnNumber': 1, '$db': 'document360-prod', 'lsid': {'id': {'$uuid': '8421f509-ab3d-46c5-bd95-aeeb56f92bad'}}, '$clusterTime': {'clusterTime': {'$timestamp': {'t': 1720738623, 'i': 3}}, 'signature': {'hash': {'$binary': {'base64': 'FRr8w8ha1WnCSjFYhE7GbTc0Lqo=', 'subType': '0'}}, 'keyId': 7356413323094523906}}}


ns|name space        = document360-prod.$cmd
numYields            = 401
durationMillis       = 157788
remote               = 10.0.32.252:52470
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-07-11T22:59:35.482+00:00
command              = {'update': 'projectLinks', 'ordered': True, 'writeConcern': {'w': 'majority'}, 'txnNumber': 2, '$db': 'document360-prod', 'lsid': {'id': {'$uuid': '5ae75814-d185-4f73-ae17-13e953eb6989'}}, '$clusterTime': {'clusterTime': {'$timestamp': {'t': 1720738620, 'i': 1}}, 'signature': {'hash': {'$binary': {'base64': '3xfHBWZDnFhhkhUa2NC/AYds8FM=', 'subType': '0'}}, 'keyId': 7356413323094523906}}}


ns|name space        = document360-prod.$cmd
numYields            = 382
durationMillis       = 155260
remote               = 10.0.32.253:58670
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-07-11T22:59:24.508+00:00
command              = {'update': 'projectLinks', 'ordered': True, 'writeConcern': {'w': 'majority'}, 'txnNumber': 62, '$db': 'document360-prod', 'lsid': {'id': {'$uuid': '2ea9359f-03f6-481a-87be-922e63df487c'}}, '$clusterTime': {'clusterTime': {'$timestamp': {'t': 1720738621, 'i': 6}}, 'signature': {'hash': {'$binary': {'base64': '2DxBZS/w5o/1HpOqUJVux4ex5DE=', 'subType': '0'}}, 'keyId': 7356413323094523906}}}


ns|name space        = document360-prod.$cmd
numYields            = 343
durationMillis       = 142111
remote               = 10.0.32.252:52410
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-07-11T22:58:22.466+00:00
command              = {'update': 'projectLinks', 'ordered': True, 'writeConcern': {'w': 'majority'}, 'txnNumber': 23, '$db': 'document360-prod', 'lsid': {'id': {'$uuid': '27b118c2-0ec4-474f-befa-4111316c653f'}}, '$clusterTime': {'clusterTime': {'$timestamp': {'t': 1720738560, 'i': 1}}, 'signature': {'hash': {'$binary': {'base64': 'X4Q0w63atcCLsOcmeMzpct837g0=', 'subType': '0'}}, 'keyId': 7356413323094523906}}}


ns|name space        = document360-prod.$cmd
numYields            = 349
durationMillis       = 139479
remote               = 10.0.32.253:57798
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-07-11T22:59:00.481+00:00
command              = {'update': 'projectLinks', 'ordered': True, 'writeConcern': {'w': 'majority'}, 'txnNumber': 5, '$db': 'document360-prod', 'lsid': {'id': {'$uuid': '5deb97e5-448d-4bd8-b352-6197d8578e22'}}, '$clusterTime': {'clusterTime': {'$timestamp': {'t': 1720738600, 'i': 8}}, 'signature': {'hash': {'$binary': {'base64': 'll0VhwSMy4G+O930tijUvxqnldg=', 'subType': '0'}}, 'keyId': 7356413323094523906}}}


ns|name space        = document360-prod.$cmd
numYields            = 333
durationMillis       = 139215
remote               = 10.0.32.253:37098
-----------------------------------------------------------------------------------------------------

```

**Example 16 - sorting by namespace**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified time frame and then pipe that to indexes to get indexes by 
 namespace and count and then cast it to a vscode tab.

```bash
% cat mongodb.log | jsonFetcher -b 20240101000000 -e 20250101000000 | indexes | vscode

**Index Aggregations** 

```
