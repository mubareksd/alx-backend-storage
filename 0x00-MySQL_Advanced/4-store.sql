-- Creates a trigger after order is made
CREATE TRIGGER item_order AFTER INSERT ON `orders`
-- updates every row that an order has been made to quantity = quantity - order
FOR EACH ROW UPDATE `items` SET quantity = quantity - New.number WHERE name=New.item_name;
