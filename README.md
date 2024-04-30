# wsaa_project_event
This project created on the basis of the knowledge acquired at ATU in the course "Web services and applications",by teacher Andrew Beatty.

# Description:
This project demonstrates creating a Web application which based on Flask server by consuming a RESTful API, perform CRUD operations on the data, accompanying web interface, using AJAX calls and link to database tables. In this application we can receive, create, change and delete events

# Steps:
1) creating repository "wsaa_project" in GitHub
2) cloning "wsaa_project" repository in Visual Studio Code and creating "server.py" file with creating data and functions
3) setting virtual environment: cmd-> local repository path -> python -m venv venv + .\venv\Scripts\activate.bat -> pip freeze +  pip install flask -> python server.py -> git add. -> git commit -m "simple server" -> git push
4) creating account in "Pythonanywhere" and hoste application online: -> in "Bash console" git clone + HTTPS key -> setting "Open Web Tab"...
5) creating "evenDAO.py" file with creating data and functions
6) creating "event.html" file with creating data and functions
7) creating "db.config.py" where we customize our database personal data
8) creating connection with mysql: pip install mysql-connector -> pip freeze > requirements.txt (creating file)
9) in pythonanywhere  create database with tables and data -> set dbconfig.py file with new data -> in bash console - git pull
10) setting database: pip install mysql.connector -> put new data in bash console (host, user, password, database)
11) lanching app in browser: http://dfgd.pythonanywhere.com/event.html


# References:
- Andrew Beatty Github: https://github.com/andrewbeattycourseware/wsaa-course-material
- Python Software Foundation. Welcome to python.org: https://www.python.org
- Python: https://realpython.com/
- Resurce with a lot necessary tools: https://www.w3schools.com/
- HTML: https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML
- Python Docs: PEP 8 – Style Guide for Python Code: https://peps.python.org/pep-0008/
- Database Connections:
https://pynative.com/python-database-connection-pooling-with-mysql/
https://overiq.com/mysql-connector-python-101/connection-pooling-using-connector-python/

#  Extra project B:
https://github.com/YuliiaRysinska/wsaa_proj_weather
In second project I created app what bases on Flask server wich  interact with an API from site "https://home.openweathermap.org". In this app we can get weather informations from different locations



