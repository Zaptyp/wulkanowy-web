# Wulkanowy Web

🌋 Unofficial VULCAN UONET+ browser client for students and their parents

![GitHub Workflow Status](https://github.com/wulkanowy/wulkanowy-web/workflows/Python%20application/badge.svg)

## Join our Discord server!

[![Discord](https://discordapp.com/api/guilds/390889354199040011/widget.png?style=banner2)](https://discord.com/invite/vccAQBr)

# Development

## 1. Install dependencies

```sh
cd backend
pip install -r requirements.txt
```
And in frontend:
```sh
cd frontend
npm install
```
## 2. Start the server

```sh
cd backend
py -m main
```
And in frontend:
```sh
cd frontend
npm run serve
```

# Docker

With docker compose

```sh
docker-compose up -d
```

Without docker compose

```sh
docker build -t wulkanowy/web .
docker run -d -p 8000:8000 wulkanowy/web
```
