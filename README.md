# Wulkanowy-web
🌋 Unofficial browser VULCAN UONET+ client for both students and their parents

![GitHub Workflow Status](https://github.com/wulkanowy/wulkanowy-web/workflows/Python%20application/badge.svg)

## Come to our discord server!
[![Discord1](https://i.imgur.com/3ljTQWy.png)](https://discord.gg/5qsEujZMdp)

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

# Docker
## With docker compose
```shell
docker-compose up -d
```
## Without docker compose
```shell
docker build -t wulkanowy/web .
docker run -d -p 8000:8000 wulkanowy/web
