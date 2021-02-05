# Wulkanowy-web
🌋 Unofficial browser VULCAN UONET+ client for both students and their parents

![GitHub Workflow Status](https://github.com/wulkanowy/wulkanowy-web/workflows/Python%20application/badge.svg)
[![Discord](https://img.shields.io/discord/390889354199040011.svg?color=#33CD56)](https://discord.gg/vccAQBr)

# Development
## 1. Install dependencies.
```shell
pip install -r requirements.txt
```
And in frontend:
```shell
npm install
```
## 2. Make migrations
```shell
python manage.py makemigrations
python manage.py migrate
```
## 3. Start the server!
```shell
python manage.py runserver
```
And in frontend:
```shell
npm run dev
```
