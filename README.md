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