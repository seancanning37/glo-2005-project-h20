CREATE TRIGGER decrementBeer
AFTER INSERT ON OrderItems
FOR EACH ROW
BEGIN
	UPDATE Beers b
	SET b.disponibility = b.disponibility - NEW.quantity 
	WHERE b.beer_id = NEW.beer_id;
END;//

CREATE TRIGGER create_rewards_card AFTER INSERT ON Customers
FOR EACH ROW 
BEGIN
	insert into RewardCard(customer_id, money_earned) values(new.id, 0.00);
END;//

CREATE TRIGGER add_reward_points AFTER INSERT ON orders
FOR EACH ROW 
BEGIN
set @temp := (SELECT r.money_earned from rewardcard r where r.customer_id = new.customer_id);
	UPDATE rewardcard SET money_earned = @temp +(new.total_price * 0.01) WHERE customer_id = new.customer_id;
END;//