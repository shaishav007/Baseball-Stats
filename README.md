# Baseball-Stats
Assignment for Blue Jays

Thank you for the opportunity. I had a lot of fun making this. I hope you like this too. For now all the data is being retrieved from different endpoints of the mlbstats api. A database is not actually required for this app to function, but models have been created in order to store the data in SQLite. They can be tweaked based on the data model, if required.

Instructions: You must have Python, Django, and Pipenv installed. If they are not, then just follow these steps. (please don't put quotes when you type a command written like this "pip install django" in powershell)

1.) Install the latest version of Python from python.org.
2.) open powershell(or any command line tool) in administrator mode
3.) Check that Python has been configured properly by just typing in "python --version"
You should see something like "Python 3.10.7". If you don't see it, it means Python has not been installed correctly. Try uninstalling and installing.
4.) Unzip or extract the zip file.
5.) In PowerShell, navigate to the directory "Stats App" and run the following commands:
"pip install pipenv"
"pipenv install django"
9.) Once both are installed, run this command: "pipenv shell"
10.) This will open a Python virtual environment where you can run "python manage.py runserver"
11.) Once the server is running, please go to a browser and enter this: "127.0.0.1:8000/homebase/overview"

COMMON ERRORS:
1.HTMLParserError
Try the command below to upgrade Django.
"pipenv install django --upgrade"
2.It might take a while to load it the first time. Try pressing Ctrl-C to stop the server and start again.

KNOWN BUGS AND ISSUES:
1. Elaborate tables don't respond well to smaller devices.
2. keyError at team-108 plateAppearances
3. Extensive error handling has not been added to this new refactored version.
