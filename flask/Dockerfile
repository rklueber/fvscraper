FROM python:3.6

RUN mkdir -p /app
COPY . /app
WORKDIR /app
RUN pip install flask pymysql flask_cors flask-mysql mysqlclient

CMD python app.py
