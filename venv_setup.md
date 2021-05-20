# *`SETUP GUIDE`*
# `1. Windows`
- open `microsoft store` (or even `google`) and easily `search` for `python` and the first thing you see is the latest version of python to install on your computer
- run `curl` [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py) `-o get-pip.py`
- run   `python get-pip.py`   on your command line 
- use   `pip install virtualenv`   to install virtual environment essentials
- now to get started just run `virtualenv venv` to create a virtual environment
- after that you can use `.\venv\scripts\activate.bat` 

# `2. Mac`
- like the setup guide of windows you can easily search it on google and download it
- the installation progress is so simple 
- run `curl` [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py) `-o get-pip.py` and `python3 get-pip.py` on your command line 
- as always `pip install virtualenv`
- `virtualenv venv`
- run `./venv/bin/activate`
# `3. Linux`
- use `sudo apt-get install python` to get the latest version of python
> ### in my experience `the command above 🙄` installs python version 2.7 🤷‍♂️
> ### so instead of this i used `sudo apt-get install python3` ✅
- use `sudo apt-get install pip` to install the latest version of pip
- `pip install virtualenv`
- `virtualenv venv` on your root directory of prject
- run `./venv/bin/activate`
- 

# `NOTICE BEFORE GET STARTED`
> `.bat` is not necessary so you can use `.\venv\scripts\activate` to activate that 

> all of this should be done in your `root` directory of project

> this environment can also be used in your other projects but it is `NOT` recommended!

> to update pip version just use `python -m pip install --upgrade pip`

> ### on linux to run the code int python`>=`3 you need to use `python3` instead of `python`
> for example: 
> ```
> python example.py (runs in python 2) ❌
> python3  example.py (runs in python 3) ✅
> ``` 
#
> ## at the end of the day you can start coding in your venv 😊

> ## go to [start](./start.md) 
