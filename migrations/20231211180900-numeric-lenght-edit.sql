ALTER TABLE `location_data`
	CHANGE COLUMN `latitude` `latitude` FLOAT(3) NOT NULL DEFAULT '0' AFTER `json`,
	CHANGE COLUMN `longitude` `longitude` FLOAT(3) NOT NULL DEFAULT '0' AFTER `latitude`;
