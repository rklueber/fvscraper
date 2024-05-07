-- Drop user if exists to avoid conflict during creation
DROP USER IF EXISTS 'scraper'@'%';

-- Create user with specific authentication method
CREATE USER 'scraper'@'%' IDENTIFIED WITH caching_sha2_password BY 'pass';

-- Grant privileges to only the prices database for better security
GRANT ALL PRIVILEGES ON prices.* TO 'scraper'@'%';

-- Apply changes immediately
FLUSH PRIVILEGES;

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS prices;

-- Select the database for subsequent operations
USE prices;

-- Create table if it does not already exist
CREATE TABLE IF NOT EXISTS prices (
    id int AUTO_INCREMENT PRIMARY KEY,
    isin varchar(255),
    price DECIMAL(15,2),
    currency varchar(10),
    datafrom varchar(12)
);

-- Add a unique index to avoid duplicate entries based on ISIN and datafrom
ALTER TABLE prices ADD UNIQUE INDEX idx_isin_datafrom (isin, datafrom);
