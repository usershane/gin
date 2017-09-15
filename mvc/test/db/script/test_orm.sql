
DROP   DATABASE test_orm;

CREATE DATABASE test_orm;

USE test_orm;

CREATE TABLE IF NOT EXISTS Person(
	nid             INT AUTO_INCREMENT PRIMARY KEY                  COMMENT 'TABLE ID',
	name		VARCHAR(10)			NOT NULL	COMMENT 'NAME',
	age		INT				NOT NULL	COMMENT 'AGE'
)ENGINE=InnoDB DEFAULT CHARSET=UTF8 AUTO_INCREMENT=1 COMMENT='Person';
