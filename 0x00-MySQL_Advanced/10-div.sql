-- creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
DELIMITER $$
CREATE FUNCTION SafeDiv (a INTEGER, b INTEGER)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE ret FLOAT;
    IF b = 0 THEN
       RETURN 0;
    END IF;
    ret = (a / b) * 1.0;
    RETURN ret;
END
$$
DELIMITER ;
