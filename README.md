## The enclosed commands are designed to closely integrate with other shell commands. The logic being what if the linux distribution had these commands built into it.

**Exaample 1**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to the linux `wc -l` command
 calculating the count of records for the specified dateframe.

```bash
% cat mongodb.log.2024-06-11T02-49-10 | jsonFetcher -b 20240601000000 -e 20240630000000 | wc -l

395596
```
**Exaample 2**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to countCommands which calculates
 the count for different commands based on the timeframe.

```bash
% cat mongodb.log.2024-06-11T02-49-10 |  jsonFetcher -b 20240601000000 -e 20240630000000 | countCommand

Count of find commands     = 5
Count of delete commands   = 0
Count of insert commands   = 1
Count of upsert commands   = 0
Count of update commands   = 1
Count of getmore commands  = 0
```

**Example 3**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to millis command which will
 sort based on durationMillis and pipe that to formatOne which will present the json in a more readable format

```bash
% cat mongodb.log.2024-06-11T02-49-10 | jsonFetcher -b 20240601000000 -e 20240630000000 | millis | formatOne

-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-06-10T22:09:17.573+00:00
command              = {'find': 'things', 'filter': {'pid': 'd88163f2-53de-4717-ad95-9ebe0c2d3cba'}, 'sort': {'sn': 1}, 'limit': 1, 'batchSize': 1, 'singleBatch': True, 'maxTimeMS': 1000, '$readPreference': {'mode': 'secondaryPreferred'}, 'readConcern': {'level': 'local'}, '$db': 'mongo-prod'}


ns|name space        = mongo-prod.things
planSummary          = IXSCAN { pid: 1, sn: -1, ts: -1 }
keysExamined         = 1
docsExamined         = 1
queryHash            = 64040B05
numYields            = 0
nreturned            = 1
durationMillis       = 39
remote               = 192.168.242.223:59302
bytesRead            = 26832
-----------------------------------------------------------------------------------------------------
```

**Example 4**

logic: The same logic as sample 3 except instead of going to stdout load directly to a vscode tab

```bash
% cat mongodb.log.2024-06-11T02-49-10 | jsonFetcher -b 20240601000000 -e 20240630000000 | millis | formatOne | vscode
```

**Example 5**

logic: Compile the average durationMillis for a given  time period and cast the output to a vscode tab

```bash
% cat mongodb.log.2024-06-11T02-49-10 | jsonFetcher -b 20240601000000 -e 20240630000000 | avgMillis | vscode

The average time for commands:  54.5 ms
```

**Example 6**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to bytesRead command which will
 sort based on bytesRead and pipe that to phead which will grab the 2 highest queries byteRead then pipe that to formatOne 
 which will present the json in a more readable format and then pipe that to a vscode tab instead of stdout

```bash
% cat mongodb.log.2024-06-11T02-49-10 | jsonFetcher -b 20240601000000 -e 20240630000000 | bytesRead | phead -r 2 | formatOne | vscode

Submission Time      = 2024-06-10T13:51:23.220+00:00
command              = {'find': 'things_journal', 'filter': {'$and': [{'pid': 'thing:io.beyonnex.smartheating.srt:eui001bc507316c3aed'}, {'to': {'$gte': 12396}}, {'from': {'$lte': 12496}}]}, 'sort': {'to': 1}, 'batchSize': 1, 'singleBatch': True, 'maxTimeMS': 1000, '$readPreference': {'mode': 'secondaryPreferred'}, 'readConcern': {'level': 'local'}, '$db': 'ddm-mongo-prod'}


ns|name space        = ddm-mongo-prod.things_journal
planSummary          = IXSCAN { pid: 1, to: -1 }
keysExamined         = 15
docsExamined         = 15
queryHash            = BAB5A1C8
numYields            = 3
nreturned            = 0
durationMillis       = 44
remote               = 192.168.242.223:39838
bytesRead            = 1660576
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-06-10T13:51:23.220+00:00
command              = {'find': 'things_journal', 'filter': {'$and': [{'pid': 'thing:io.beyonnex.smartheating.srt:eui001bc507316c3aed'}, {'to': {'$gte': 12396}}, {'from': {'$lte': 12496}}]}, 'sort': {'to': 1}, 'batchSize': 1, 'singleBatch': True, 'maxTimeMS': 1000, '$readPreference': {'mode': 'secondaryPreferred'}, 'readConcern': {'level': 'local'}, '$db': 'ddm-mongo-prod'}


ns|name space        = ddm-mongo-prod.things_journal
planSummary          = IXSCAN { pid: 1, to: -1 }
keysExamined         = 15
docsExamined         = 15
queryHash            = BAB5A1C8
numYields            = 3
nreturned            = 0
durationMillis       = 44
remote               = 192.168.242.223:39838
bytesRead            = 1660576
-----------------------------------------------------------------------------------------------------
```

**Example 7**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to appName to get all the appNames
 with their count.

```bash
% cat mongodb.log.2024-06-11T02-49-10 | jsonFetcher -b 20240601000000 -e 20240630000000 | appName | vscode


     Count   App Name  
     -----   ----------------------
     14953   Document360-UserWebsite
      5207   API       
      4134   AlgoliaIndexGenerator
      1236   APIHub    
       991   mongot initial sync and session refresh
       616   BrokenLinkAnalytics.LinkIdentifier
       358   Admin-WebAPI
       224   Document360-KB-API
        94   mongosync, v: 1.4.1, i: coordinator, cl: src, cm: 16875b92, g: go1.19.10, cp: gc, p: 0776473c-39cb-4075-954c-31aee2c9f532
        87   mongot steady state
        78   OplogFetcher
        22   MongoDB CPS Module v13.17.2.8878 (git: 70c0b932f47f4f0b3e82a75e223f39ed9635b47f)
        22   app-services|triggers-qugyd
        21   ExportPDF 
        12   Studio 3T 
        10   AuditingNotificationGenerator
         9   MongoDB Compass
         9   MongoDB Automation Agent v13.17.2.8878 (git: 70c0b932f47f4f0b3e82a75e223f39ed9635b47f)
         8   DailyJobs 
         5   mongosh 1.6.1
         4   mongoexport
         4   Identity  
         3   ImportExportJobs
         3   app-services|crm_api-vgkne
         3   MongoDB Automation Agent v13.16.2.8826 (git: 36d72fa13b663f402e1285ab8458536766897530)
         1   LinkStatusChecker
         1   app-services|crm_triggers-kvvub
         1   AnalyticsProcessor
         1   app-services|custom-domain-app-manager-us-jcubh
         1   ScheduledLinkStatusChecker
         1   MongoDB Monitoring Module v13.17.2.8878 (git: 70c0b932f47f4f0b3e82a75e223f39ed9635b47f)
         1   SEODescriptionGenerator
```

**Example 8**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified dateframe and then pass that to docsExamined this will return
 the full json ordered by docsExamined, then takes the top 3 because of phead, pipe that to formatOne to increase readability
 and then pipe it to a vscode tab.
 
```bash
% cat mongodb.log.2024-06-11T02-49-10 | jsonFetcher -b 20240601000000 -e 20240630000000 | docsExamined | phead -r 3 | formatOne | vscode

Submission Time      = 2024-06-10T13:51:23.220+00:00
command              = {'find': 'things_journal', 'filter': {'$and': [{'pid': 'thing:io.beyonnex.smartheating.srt:eui001bc507316c3aed'}, {'to': {'$gte': 12396}}, {'from': {'$lte': 12496}}]}, 'sort': {'to': 1}, 'batchSize': 1, 'singleBatch': True, 'maxTimeMS': 1000, '$readPreference': {'mode': 'secondaryPreferred'}, 'readConcern': {'level': 'local'}, '$db': 'ddm-mongo-prod'}


ns|name space        = ddm-mongo-prod.things_journal
planSummary          = IXSCAN { pid: 1, to: -1 }
keysExamined         = 15
docsExamined         = 15
queryHash            = BAB5A1C8
numYields            = 3
nreturned            = 0
durationMillis       = 44
remote               = 192.168.242.223:39838
bytesRead            = 1660576
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-06-10T13:51:23.220+00:00
command              = {'find': 'things_journal', 'filter': {'$and': [{'pid': 'thing:io.beyonnex.smartheating.srt:eui001bc507316c3aed'}, {'to': {'$gte': 12396}}, {'from': {'$lte': 12496}}]}, 'sort': {'to': 1}, 'batchSize': 1, 'singleBatch': True, 'maxTimeMS': 1000, '$readPreference': {'mode': 'secondaryPreferred'}, 'readConcern': {'level': 'local'}, '$db': 'ddm-mongo-prod'}


ns|name space        = ddm-mongo-prod.things_journal
planSummary          = IXSCAN { pid: 1, to: -1 }
keysExamined         = 15
docsExamined         = 15
queryHash            = BAB5A1C8
numYields            = 3
nreturned            = 0
durationMillis       = 44
remote               = 192.168.242.223:39838
bytesRead            = 1660576
-----------------------------------------------------------------------------------------------------

Submission Time      = 2024-06-10T22:09:17.573+00:00
command              = {'find': 'things_snaps', 'filter': {'pid': 'thing:io.beyonnex.room-group:d88163f2-53de-4717-ad95-9ebe0c2d3cba'}, 'sort': {'sn': 1}, 'limit': 1, 'batchSize': 1, 'singleBatch': True, 'maxTimeMS': 1000, '$readPreference': {'mode': 'secondaryPreferred'}, 'readConcern': {'level': 'local'}, '$db': 'ddm-mongo-prod'}


ns|name space        = ddm-mongo-prod.things_snaps
planSummary          = IXSCAN { pid: 1, sn: -1, ts: -1 }
keysExamined         = 1
docsExamined         = 1
queryHash            = 64040B05
numYields            = 0
nreturned            = 1
durationMillis       = 39
remote               = 192.168.242.223:59302
bytesRead            = 26832
-----------------------------------------------------------------------------------------------------
```

**Example 9**

logic: using the linux `cat` function pipe the contents of the mongod logs into the jsonFetcher which will use datetime
 to calculate which json entries correspond to the specified date time frame and then pass that to convertLogs to convert
 logs 5.+ to 4.4 and before which will pipe that to a modified version of generate_mplot_logs.py that permits input from 
 stdin/pipe, by generating a bash script, calling it and piping to vscode

```bash
% cat mongodb.log.2024-06-11T02-49-10 | jsonFetcher -b 20240101000000 -e 20250101000000 |  convertLogs | mkConsh; bash connStats.sh | vscode

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

**Example 11 - piping into multiple filters collScans, millis -- collections scans sorted by millisreconds high to low**

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



# Add to your bash shell
```bash
export MSHELL=/home/kadmin/Dropbox/python/vcode-loader
export PYTHON_BIN=python3
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
```
