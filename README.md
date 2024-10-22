<p align="center">
  <img src="https://avatars.githubusercontent.com/u/27146352?s=200&v=4" />
</p>
<h1 align="center">Wulkanowy Web</h1>

<h4 align="center">🌋 Unofficial VULCAN UONET+ browser client for students and their parents</h4>

# Development

## 1. Install dependencies
Backend:
```sh
cd backend
git submodule init
git submodule update
pip install -r requirements.txt
```
Frontend:
```sh
cd frontend
npm install
```
## 2. Start the server
Backend:
```sh
cd backend
py -m main
```
Frontend:
```sh
cd frontend
npm run serve
```

# Features
* logging in using the email, password
* light and dark theme
* school and teachers informations
* conferences

# Api
This project uses the project [Marioneq4958/uonetplus_api](https://github.com/Marioneq4958/uonetplus_api). Check [documentation](https://github.com/Zaptyp/wulkanowy-web/wiki)

# License

This project is licensed under the Apache License 2.0
