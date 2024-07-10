-- SQL script for creating stored procedure
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE p_id INT;
	SELECT id INTO p_id FROM projects WHERE name = project_name;
	IF p_id IS NULL THEN
		INSERT INTO projects (name) VALUES (project_name);
		SET p_id = LAST_INSERT_ID();
	END IF;
	UPDATE corrections c set c.score = score WHERE c.user_id = user_id AND c.project_id = p_id; 

END $$

DELIMITER ;
