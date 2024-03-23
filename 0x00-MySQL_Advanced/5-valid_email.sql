-- creates a trigger that resets the attribute valid_email only when the email has been changed
DROP TRIGGER IF EXISTS email_reset
DELIMITER ;;
CREATE TRIGGER email_reset
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email
        SET NEW.valid_email = 0;
    ELSE
        SET NEW.valid_email = NEW.valid_email;
    END IF
END ;;
DELIMITER ;