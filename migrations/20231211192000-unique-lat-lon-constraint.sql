ALTER TABLE `location_data`
	CHANGE COLUMN `longitude` `longitude` FLOAT NULL DEFAULT '0' AFTER `latitude`,
	ADD UNIQUE INDEX `Index 2` (`latitude`, `longitude`);