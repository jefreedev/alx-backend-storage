-- SQL Script that reates a table: users
-- with the following attributes:
--	id
--	email
--	name
-- If the table already exists, this script should not fail
-- This script can be executed in any db
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
