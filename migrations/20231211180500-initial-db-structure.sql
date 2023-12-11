CREATE TABLE IF NOT EXISTS `location_data` (
    `ID` INT NOT NULL AUTO_INCREMENT,
	`json` JSON NOT NULL,
	`latitude` FLOAT NOT NULL DEFAULT 0,
	`longitude` FLOAT NOT NULL DEFAULT 0,
	PRIMARY KEY (`ID`)
)
COLLATE='utf8_general_ci'
;

