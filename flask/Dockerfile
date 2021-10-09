FROM python:3.6

RUN mkdir -p /app
COPY flask/ /app
WORKDIR /app
RUN pip install flask pymysql flask_cors flask-mysql mysqlclient

CMD python app.py
