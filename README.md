# project-event
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
10) lunch app in web browsers 
# wsaa_project
The main goal of the project is create a Web Application in Python using Flask which links with API from site https://home.
openweathermap.org/.


# Steps:
1) lunch/activate virtual machine and install packages and requirement file(python -m venv venv -> .\venv\Scripts\activate.
bat ->pip install requests python-dotenv Flask ->py -m pip install -U pip ->pip freeze > requirements.txt)
2) creating git ignore file to hide ".venv", ".env"
3) register on https://home.openweathermap.org and put api_key  to ".env" file
4) create css code  in  "static folder"
5) create html code in  "templates folder"
6) creating weather function in "weather.py" file
7) lunch Flask with code in "server.py"
8) setting production mode: pip install waitress -> pip freeze > requirements.txt
9) creating "weather.py" to get API
10) lunch app in browser
