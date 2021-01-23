# Wulkanowy-web
🌋 Unofficial browser VULCAN UONET+ client for both students and their parents

![GitHub Workflow Status](https://github.com/wulkanowy/wulkanowy-web/workflows/Python%20application/badge.svg)
[![Discord](https://img.shields.io/discord/390889354199040011.svg?color=#33CD56)](https://discord.gg/vccAQBr)

# Development
## 1. Install webpack and dependencies.
```shell
npm install webpack
pip install -r requirements.txt
```
## 2. Create .env and make migrations
In the .env file put the code:
```shell
SECRET_KEY = writeanythinghere
```
After saving the files, we migrate with these commands:
```shell
python manage.py makemigrations
python manage.py migrate
```
and modify the .envsample file as you would the .env file
THE SECRET KEY MUST BE THE SAME
## 3. Start the server!
```shell
npm run dev
python manage.py runserver
```
or if you run Windows you can run:
```shell
runserver.bat
```
