FROM nikolaik/python-nodejs:python3.9-nodejs15

ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY frontend/package-lock.json .
COPY frontend/package*.json ./frontend/

RUN npm install

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/* ./app/
COPY app/API/* ./app/API/
COPY app/migrations/* ./app/migrations/
COPY frontend/* ./frontend/
COPY frontend/src/* ./frontend/src/
COPY frontend/migrations/* ./frontend/migrations/
COPY frontend/static/frontend/* ./frontend/static/frontend/
COPY frontend/static/frontend/css/* ./frontend/static/frontend/css/
COPY frontend/static/frontend/images/* ./frontend/static/frontend/images/
COPY frontend/templates/frontend/* ./frontend/templates/frontend/
COPY wulkanowy/* ./wulkanowy/
COPY manage.py .

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

ENTRYPOINT [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]