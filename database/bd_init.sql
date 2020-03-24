CREATE DATABASE IF NOT EXISTS glo2005;

USE glo2005;

CREATE TABLE IF NOT EXISTS Customers
{
	id INTEGER NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	phone VARCHAR(100),
	email VARCHAR(100) NOT NULL UNIQUE,
	login_username VARCHAR(100) NOT NULL UNIQUE,
	login_password VARCHAR(100) NOT NULL,
	address_line_1 VARCHAR(100),
	address_line_2 VARCHAR(100),
	city VARCHAR(100),
	country VARCHAR(100),
	PRIMARY KEY (id)
};

CREATE TABLE IF NOT EXISTS Orders
{
	order_id INTEGER NOT NULL AUTO_INCREMENT,
	customer_id INTEGER NOT NULL,
	order_date Date,
	status VARCHAR(100),
	total_price DECIMAL(10, 2),
	comment VARCHAR(100),
	PRIMARY KEY (order_id),
	FOREIGN KEY (customer_id) REFERENCES Customers (id) 
		ON DELETE CASCADE
		ON UPDATE CASCADE
};

CREATE IF NOT EXISTS OrderItems
{
	item_id INTEGER NOT NULL AUTO_INCREMENT,
	order_id INTEGER NOT NULL,
	beer_id INTEGER NOT NULL,
	quantity INTEGER NOT NULL,
	beer_price DECIMAL(10, 2) NOT NULL,
	PRIMARY KEY (item_id, order_id),
	FOREIGN KEY (order_id) REFERENCES Orders (order_id)
		ON DELETE CASCADE,
	FOREIGN KEY (beer_id) REFERENCES Beers (beer_id)
		ON DELETE CASCADE,
	FOREIGN KEY (beer_price) REFERENCES Beers (beer_id)
		ON DELETE CASCADE
};

CREATE IF NOT EXISTS Beers
{
	beer_id INTEGER NOT NULL AUTO_INCREMENT,
	brand_id INTEGER NOT NULL,
	beer_name VARCHAR(100) NOT NULL,
	beer_type INTEGER,
	alcohol_percentage DECIMAL(3, 2) NOT NULL,
	ibu INTEGER,
	volume INTEGER,
	country VARCHAR(100),
	beer_price DECIMAL(10, 2) NOT NULL,
	description VARCHAR(250),
	PRIMARY KEY (beer_id),
	FOREIGN KEY (brand_id) REFERENCES Brands (brand_id)
		ON DELETE CASCADE,
	FOREIGN KEY (beer_type) REFERENCES BeerTypes (type_id)
};

CREATE IF NOT EXISTS Brands
{
	brand_id INTEGER NOT NULL AUTO_INCREMENT,
	brand_name VARCHAR(100) NOT NULL,
	brand_phone VARCHAR(100),
	brand_address VARCHAR(100),
	brand_country VARCHAR(100)
};

CREATE IF NOT EXISTS BeerTypes
{
	type_id INTEGER NOT NULL AUTO_INCREMENT,
	type_name VARCHAR(100)
};

SHOW DATABASES;