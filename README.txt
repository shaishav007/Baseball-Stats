README
Thank you for the opportunity. I had a lot of fun making this. I hope you like this too. For now all the data is being retrieved from different endpoints of the mlbstats api. A database is not actually required for this app to function but models have been created in order to store the data in SQLite. They can be tweaked based on the data-model if required. 

A preliminary idea of the data models is here - https://excalidraw.com/#json=FEC7YA_NUKDl-pm3CU479,LZYJhfXOhJE5B-y0lPFkcw


INSTRUCTIONS(please don't put quotes when you type a command written like this "pip install django" in powershell)
you must have python, django and pipenv installed. If they are not then just follow these steps
1. install the latest version of python from python.org 
2. open powershell(or any command line tool) in administrator mode
3. check python has been configured properly by just typing in "python --version"
 - you should see something like - "Python 3.10.7"
  if you don't see it, it means python has not been installed correctly, try uninstalling and installing
4. extract the zip file
5. in powershell navigate to the directory "Stats App" and run the following commands
6."pip install pipenv"
7."pipenv install django"
9. once both are installed run this command -  "pipenv shell"
10.it will open a python virtual environment where you can run - "python manage.py runserver"
11. once the server is running please go to a browser and enter this "127.0.0.1:8000/homebase/overview"

COMMON ERRORS 
1.HTMLParserError
try the command below to upgrade Django
2.pipenv install django --upgrade
-it might take a while to load it the first time. Try pressing Ctrl-C to stop the server and start again.

known bugs and issues to be fixed
1. elaborate tables don't respond well to smaller devices, need to fix it
2. keyError at team-108
plateAppearances 
3. extensive error handling has not been added to this new refactored version. Gotta add that.
4. The order of the leagues is different from the template provided