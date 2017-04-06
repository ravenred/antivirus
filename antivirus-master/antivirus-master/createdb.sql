CREATE DATABASE `known_hash` /*!40100 DEFAULT CHARACTER SET utf8 */;

CREATE TABLE `filedb` (
  `knownfile` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `known_hash`.`filedb`
(`knownfile`)
VALUES
('C:\Users\Ian\Documents\testav\fileThree.txt');
