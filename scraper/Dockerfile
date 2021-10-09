FROM python:3.6

COPY scraper/requirements.txt /scrapy/requirements.txt
RUN pip install -r /scrapy/requirements.txt
RUN rm /scrapy/requirements.txt

RUN apt update
RUN apt install wait-for-it

COPY scraper/ /scrapy

WORKDIR /scrapy
