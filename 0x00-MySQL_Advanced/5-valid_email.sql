-- Drop trigger validate_email if it exists
DROP TRIGGER IF EXISTS `validate_email`;
-- Creates trigger validate_email
DELIMITER $$ ;
CREATE TRIGGER IF NOT EXISTS validate_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
       SET NEW.valid_email = 0;
    END IF;
END;$$
DELIMITER ;
