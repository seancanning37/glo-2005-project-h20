DELIMITER //
CREATE TRIGGER decrementBeer
AFTER INSERT ON OrderItems
FOR EACH ROW
BEGIN
	UPDATE Beers b
	SET b.disponibility = b.disponibility - NEW.quantity 
	WHERE b.beer_id = NEW.beer_id;
END;//
DELIMITER ;
