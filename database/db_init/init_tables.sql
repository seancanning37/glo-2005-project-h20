
CREATE TABLE IF NOT EXISTS Customers
(
	id INTEGER NOT NULL AUTO_INCREMENT,
	name varchar(100) NOT NULL,
	phone VARCHAR(100),
	email VARCHAR(100) NOT NULL UNIQUE,
	username VARCHAR(100) UNIQUE,
	password VARCHAR(100) NOT NULL,
	address_line_1 VARCHAR(100),
	address_line_2 VARCHAR(100),
	city VARCHAR(100),
	country VARCHAR(100),
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Orders
(
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
);

CREATE INDEX customerID ON Orders (customer_id);

CREATE TABLE IF NOT EXISTS Brands
(
	brand_id INTEGER NOT NULL UNIQUE KEY,
	brand_name VARCHAR(100) NOT NULL,
	brand_phone VARCHAR(100),
	brand_address VARCHAR(100),
	brand_city VARCHAR(100),
	brand_country VARCHAR(100),
	PRIMARY KEY (brand_id)
);

CREATE TABLE IF NOT EXISTS Types
(
    type_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE KEY,
	type_name VARCHAR(100),
	PRIMARY KEY (type_id)
);

CREATE TABLE IF NOT EXISTS Styles
(
    style_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE KEY,
    style_name VARCHAR(100),
    PRIMARY KEY (style_id)
);


CREATE TABLE IF NOT EXISTS Beers
(
	beer_id INTEGER NOT NULL UNIQUE KEY,
	brand_id INTEGER,
	beer_name VARCHAR(100) NOT NULL,
	abv DECIMAL(4, 2) NOT NULL,
	ibu INTEGER,
	volume INTEGER,
	style_id INTEGER,
	type_id INTEGER,
	beer_price DECIMAL(10, 2) NOT NULL,
	disponibility INTEGER NOT NULL,
	description VARCHAR(250),
	PRIMARY KEY (beer_id),
	FOREIGN KEY (style_id) REFERENCES Styles (style_id),
	FOREIGN KEY (type_id) REFERENCES Types (type_id)
);

CREATE INDEX beerStyle ON Beers (style_id) USING HASH;

CREATE INDEX beerType ON Beers (type_id) USING HASH;

CREATE INDEX BeerPrice ON Beers (beer_price) USING BTREE;

CREATE INDEX beerBrand ON Beers (brand_id) USING HASH;

CREATE TABLE IF NOT EXISTS OrderItems
(
	item_id INTEGER NOT NULL AUTO_INCREMENT,
	order_id INTEGER NOT NULL,
	beer_id INTEGER NOT NULL,
	quantity INTEGER NOT NULL,
	PRIMARY KEY (item_id),
	FOREIGN KEY (order_id) REFERENCES Orders (order_id)
		ON DELETE CASCADE,
	FOREIGN KEY (beer_id) REFERENCES Beers (beer_id)
		ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Passwords
(
    customer_id INTEGER NOT NULL UNIQUE,
    password VARCHAR(72),
    FOREIGN KEY (customer_id) REFERENCES Customers (id)
);

