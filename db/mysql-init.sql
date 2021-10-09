CREATE DATABASE IF NOT EXISTS prices;
USE prices;
CREATE TABLE IF NOT EXISTS prices (id int AUTO_INCREMENT PRIMARY KEY, isin varchar(255), price DECIMAL(15,2), currency varchar(10), datafrom varchar(12));
CREATE USER 'scraper'@'%' IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON *.* TO 'scraper'@'%';
FLUSH PRIVILEGES;
ALTER TABLE prices ADD UNIQUE INDEX(isin, datafrom);