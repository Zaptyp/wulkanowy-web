# Wulkanowy-web
🌋 Unofficial browser VULCAN UONET+ client for both students and their parents

![GitHub Workflow Status](https://github.com/wulkanowy/wulkanowy-web/workflows/Python%20application/badge.svg)
[![Discord](https://img.shields.io/discord/390889354199040011.svg?color=#33CD56)](https://discord.gg/vccAQBr)

# Development
## 0. Automatic installation (WINDOWS ONLY)
If you don't want to enter commands just run
```shell
install.exe
```
If that doesn't work, run the file:
```shell
install.bat
```
Which is in the batch folder
After this installation, just follow the 3rd step
## 1. Install dependencies.
```shell
pip install -r requirements.txt
```
And in frontend:
```shell
npm install
```
## 2. Create .env and make migrations
In the .env file put the code:
```shell
SECRET_KEY = VULCANWEBKEY
```
After saving the files, we migrate with these commands:
```shell
python manage.py makemigrations
python manage.py migrate
```
## 3. Start the server!
```shell
npm run dev
python manage.py runserver
```
or if you run Windows you can run:
```shell
runserver.bat
```