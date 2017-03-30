CREATE DATABASE `known_hash` /*!40100 DEFAULT CHARACTER SET utf8 */;

CREATE TABLE `hashes` (
  `md5` varchar(250) NOT NULL,
  PRIMARY KEY (`md5`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `known_hash`.`hashes`
(`md5`)
VALUES
("ee1a7267fe3e305280a505bdf6369b74");