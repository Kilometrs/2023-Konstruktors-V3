ALTER TABLE `location_data`
	ADD COLUMN `date` VARCHAR(255) NOT NULL DEFAULT '0' AFTER `ID`;