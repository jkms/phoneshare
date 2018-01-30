CREATE DATABASE phonebank;
CREATE USER 'phonebank'@'%' IDENTIFIED BY 'phonebank';

GRANT ALL PRIVILEGES ON phonebank.* TO 'phonebank'@'%';

CREATE TABLE `phonebank`.`e164` ( `hash` CHAR(64) NOT NULL , `value` TEXT NOT NULL , PRIMARY KEY (`hash`)) ENGINE = InnoDB COMMENT = 'e164 Hash Table';
CREATE TABLE `phonebank`.`campaign` ( `camp_id` INT NOT NULL , `name` TEXT NOT NULL , `description` TEXT NOT NULL , PRIMARY KEY (`camp_id`)) ENGINE = InnoDB COMMENT = 'Campaign Table';


FLUSH PRIVILEGES;