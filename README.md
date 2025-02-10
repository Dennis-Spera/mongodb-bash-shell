## The package is designed to interact with the other commands found documented here. Concidering this is meant to be used as a pipeline, these pipelines can also interact with other linux command when used in the correct context. The difference here is the piplines stdin/stdout are formatted json instead of plan text

**Setup**

**test in virtual environment**


**Run it in a virtual Environmental**
```bash
# Create the virtual environment
pip install virtualenv
mkdir mshell
cd mshell
python3 -m venv mongo-shell
cd mongo-shell
source bin/activate
git clone https://github.com/Dennis-Spera/mongodb-bash-shell.git
cd mongodb-bash-shell
pip install -r requirements.txt
bash compile.sh
bash promote.sh
```

**Go right into your live python environment**
```bash
git clone https://github.com/Dennis-Spera/mongodb-bash-shell.git
cd mongodb-bash-shell
pip install -r requirements.txt
bash compile.sh
bash promote.sh
```

**Inventory of files**

 - **appName** - a list of all the apps for the specified time period.
 - **bytesRead** - sort json by bytes read
 - **collScans** - list json that is a collection scan
 - **docsExamined** - sort json by docsExamined
 - **drivers** - aggegate counts for all drivers used during a time period
 - **formatOne** - format the piped json displaying releavant data stripping off unnecessary data 
 - **jsonFetcher** - returns all the json that fall between a begin date and end date date format YYYYMMDDHRMNSS
 - **keysExamined** - sort json by keysExamined
 - **millis** - sort json by milliseconds
 - **nsIndexes** - list the indexes used by namespace with a count
 - **ns** - sort json by namespace
 - **phead** - the installed head command sends a `SIGTERM` to cat command, this is the python version
 - **queryHash** - list query shapes (query shapes) and counts
 - **cpuc** - sort json by cpu nano seconds used highest to lowest
 - **nsCount** - aggregate count of name spaces
 - **nsCountUser** - aggregate count of name spaces by user
 - **prettyJson** - pretty print json


**Example - get the json with the 2 highest queries bytes read, format the output**

```bash
% cat mongodb.log |  jsonFetcher -b 20200601000000 -e 20250630000000 | millis | formatOne 
```

**Example - get the json with the 2 highest queries bytes read, format the output**

```bash
% cat mongodb.log | bytesRead | phead -r 2 | formatOne 
```

**Example - get the app names and count**

```bash
% cat mongodb.log | appName 
```

**Example - order the json by docExamined return the top 3 and format the text**
 
```bash
% cat mongodb.log | docsExamined | phead -r 3 | formatOne 
```

**Example - piping into multiple filters collScans, millis -- collections scans sorted by millisreconds high to low**

```bash
% cat mongodb.log | collScans | millis | phead -r 3 | formatOne 
```

**Example - list drivers and counts**

```bash
% cat mongodb.log | drivers 
```

**Example - sorting by namespace**

```bash
% cat mongodb.log | millis | phead -r 10 | ns | formatOne 
```

**Example - extract indexes with counts**

```bash
% cat mongodb.log | nsIndexes 
```

**Addendum**

If you get this error

Traceback (most recent call last):
  File "PyInstaller/loader/pyiboot01_bootstrap.py", line 20, in <module>
  File "PyInstaller\loader\pyimod02_importers.py", line 614, in install
RuntimeError: Bootloader did not set sys._pyinstaller_pyz!
[16737] Failed to execute script 'pyiboot01_bootstrap' due to unhandled exception!

```bash
try:
 pip uninstall pyinstaller
 pip install pyinstaller
 bash compile.sh
 bash promote.sh
``` 
