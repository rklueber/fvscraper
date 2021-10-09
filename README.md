This repo is for the purpose of demonstrating how to deploy a Scrapy web scraper and a MySQL database together, with docker-compose. It scrapes Flossbach von Storch ONE prices. In order to test it out, clone the repo and execute the following command:

    docker-compose up --build -d

Once MySQL is ready, you can execute the following line:

    docker run -it --network=fvscrape_scrapy_mysql_net mysql mysql -uroot -ppass -hdb

And when you're in the MySQL interpreter, execute something like this:

    use prices;
    select * from prices;

To start debug scrapy

    docker exec -it scrapy bash 

Adding PATH

    $env:Path += ";C:\Users\r\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts"
