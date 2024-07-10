-- SQL script to create a trigger
CREATE TRIGGER update_quantity AFTER INSERT ON orders 
FOR EACH ROW UPDATE items SET quantity = items.quantity - NEW.number WHERE items.name = NEW.item_name;
