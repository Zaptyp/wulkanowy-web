# Wulkanowy-web
🌋 Przeglądarkowy klient dzienniczka VULCAN UONET+ dla ucznia i rodzica

![GitHub Workflow Status](https://github.com/wulkanowy/wulkanowy-web/workflows/Python%20application/badge.svg)
[![Discord](https://img.shields.io/discord/390889354199040011.svg?color=#33CD56)](https://discord.gg/vccAQBr)

# Development
## 1. Install dependencies.
```shell
pip install -r requirments.txt
```
## 2. Create database and .env
```shell
python manage.py makemigrations
python manage.py migrate
```
and modify the .envsample file.
## 3. Start the server!
```shell
python manage.py runserver
```