-- creates a trigger that decreases the quantity of an item after adding a new order
DROP TRIGGER IF EXISTS reduce_item
DELIMITER ..
CREATE TRIGGER reduce_item
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
        SET quantity = quantity - NEW.quantity
        WHERE name = NEW.name
END..
DELIMITER ;