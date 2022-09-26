FROM python:latest

WORKDIR /app

RUN mkdir -p /app/static/css
RUN mkdir -p /app/static/images
COPY /static/css /app/static/css
COPY /static/images /app/static/images
RUN mkdir /app/templates
COPY /templates /app/templates
COPY requirements.txt .
COPY app.py .

RUN pip install -r requirements.txt

CMD flask run -h 0.0.0.0 -p 5000
