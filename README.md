This repo is for the purpose of demonstrating how to deploy a Scrapy web scraper and a MySQL database together, with docker-compose. It scrapes Flossbach von Storch ONE prices. In order to test it out, clone the repo and execute the following command:

    docker-compose up --build -d

It starts three dockers

1) db: the mysql backend
2) scraper: fetches recent prices fro FvS ONE fonds
3) flask: provides JSON data for Portfolio Performance

Once MySQL is ready, you can execute the following line:

    docker run -it --network=fvscraper_scrapy_mysql_net mysql mysql -uroot -ppass -hdb

And when you're in the MySQL interpreter, execute something like this:

    use prices;
    select * from prices;

To start debug scrapy

    docker exec -it scrapy bash 
    scrapy.exe shell https://lu.fvsinvest.lu/en/other/

To see all results stored in the data base

    http://host.ip:5000/prices

To see prices for ISIN LU2040452752

    http://host.ip:5000/prices/LU2040452752

Adding PATH

    $env:Path += ";C:\Users\r\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts"


http://10.0.10.150:5001/onvista/getHistoricPrices?isin={ISIN}&days=90
$.prices[*].datum
dd.MM.yyyy  
$.prices[*].schluss 
$.prices[*].tief    
$.prices[*].hoch    
$.prices[*].volumen

 