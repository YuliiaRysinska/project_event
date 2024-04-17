# wsaa_project
This project was create on the basis of the knowledge acquired at ATU in the course "Web services and applications" , teacher Andrew Beatty.

# Steps:
1) creating repository "wsaa_project" in GitHub
2) cloning "wsaa_project" repository in Visual Studio Code and creating "server.py" file
3) setting virtual environment: cmd-> local repository path -> python -m venv venv + .\venv\Scripts\activate.bat -> pip freeze +  pip install flask -> python server.py -> git add. -> git commit -m "simple server" -> git push
4) creating account in "Pythonanywhere" -> in "Bash console" git clone + HTTPS key -> setting "Open Web Tab"...
5) creating evenDAO.py, db.config.py, event.html with data
6) creating connection with mysql: pip install mysql-connector -> pip freeze > requirements.txt (creating file)
7) git add . -> git commit -m "real server" -> git push
8) in pythonanywhere  create database with tables and data -> set dbconfig.py file with new data -> in bash console - git pull
9) setting database: pip install mysql.connector -> put new data in bash console (host, user, password, database)
10) 