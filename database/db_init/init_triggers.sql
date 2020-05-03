DELIMITER //
CREATE TRIGGER decrementBeer
AFTER INSERT ON OrderItems
FOR EACH ROW
BEGIN
	UPDATE BEERS B
	SET B.disponibility = B.disponibility - NEW.quantity 
	where B.beer_id = NEW.beer_id;
END;//
DELIMITER ;