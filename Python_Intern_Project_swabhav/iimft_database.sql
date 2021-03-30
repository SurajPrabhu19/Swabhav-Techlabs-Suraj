-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.21 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table pyintern.booking
CREATE TABLE IF NOT EXISTS `booking` (
  `booking_id` int NOT NULL AUTO_INCREMENT,
  `booking_date` datetime NOT NULL,
  `total_amount` float NOT NULL,
  `event_id` int DEFAULT NULL,
  `exhibitor_id` int DEFAULT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `event_id` (`event_id`),
  KEY `exhibitor_id` (`exhibitor_id`),
  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `eventt` (`event_id`),
  CONSTRAINT `booking_ibfk_2` FOREIGN KEY (`exhibitor_id`) REFERENCES `exhibitor` (`exhibitor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table pyintern.booking: ~2 rows (approximately)
DELETE FROM `booking`;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` (`booking_id`, `booking_date`, `total_amount`, `event_id`, `exhibitor_id`) VALUES
	(1, '2020-04-10 00:00:00', 15000, 1, 2),
	(2, '2021-02-15 00:00:00', 20000, 2, 2);
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;

-- Dumping structure for table pyintern.bookstall_map
CREATE TABLE IF NOT EXISTS `bookstall_map` (
  `book_stall_map_id` int NOT NULL AUTO_INCREMENT,
  `booking_id` int DEFAULT NULL,
  `event_id` int DEFAULT NULL,
  `stall_id` int DEFAULT NULL,
  PRIMARY KEY (`book_stall_map_id`),
  KEY `booking_id` (`booking_id`),
  KEY `event_id` (`event_id`),
  KEY `stall_id` (`stall_id`),
  CONSTRAINT `bookstall_map_ibfk_1` FOREIGN KEY (`booking_id`) REFERENCES `booking` (`booking_id`),
  CONSTRAINT `bookstall_map_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `eventt` (`event_id`),
  CONSTRAINT `bookstall_map_ibfk_3` FOREIGN KEY (`stall_id`) REFERENCES `stall` (`stall_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table pyintern.bookstall_map: ~2 rows (approximately)
DELETE FROM `bookstall_map`;
/*!40000 ALTER TABLE `bookstall_map` DISABLE KEYS */;
INSERT INTO `bookstall_map` (`book_stall_map_id`, `booking_id`, `event_id`, `stall_id`) VALUES
	(1, 2, 2, 1),
	(2, 1, 1, 2);
/*!40000 ALTER TABLE `bookstall_map` ENABLE KEYS */;

-- Dumping structure for table pyintern.country
CREATE TABLE IF NOT EXISTS `country` (
  `country_id` int NOT NULL AUTO_INCREMENT,
  `country_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`country_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table pyintern.country: ~3 rows (approximately)
DELETE FROM `country`;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` (`country_id`, `country_name`) VALUES
	(1, 'India'),
	(2, 'Australia'),
	(3, 'United States');
/*!40000 ALTER TABLE `country` ENABLE KEYS */;

-- Dumping structure for table pyintern.eventt
CREATE TABLE IF NOT EXISTS `eventt` (
  `event_id` int NOT NULL AUTO_INCREMENT,
  `event_name` varchar(255) DEFAULT NULL,
  `booking_start_date` datetime NOT NULL,
  `event_start_date` datetime NOT NULL,
  `event_end_date` datetime NOT NULL,
  `venue_id` int DEFAULT NULL,
  PRIMARY KEY (`event_id`),
  KEY `venue_id` (`venue_id`),
  CONSTRAINT `eventt_ibfk_1` FOREIGN KEY (`venue_id`) REFERENCES `venue` (`venue_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table pyintern.eventt: ~2 rows (approximately)
DELETE FROM `eventt`;
/*!40000 ALTER TABLE `eventt` DISABLE KEYS */;
INSERT INTO `eventt` (`event_id`, `event_name`, `booking_start_date`, `event_start_date`, `event_end_date`, `venue_id`) VALUES
	(1, 'iimft_1', '2020-03-10 00:00:00', '2020-03-20 00:00:00', '2020-03-30 00:00:00', 1),
	(2, 'iimft_2', '2020-04-10 00:00:00', '2020-04-20 00:00:00', '2020-04-30 00:00:00', 2);
/*!40000 ALTER TABLE `eventt` ENABLE KEYS */;

-- Dumping structure for table pyintern.exhibitor
CREATE TABLE IF NOT EXISTS `exhibitor` (
  `exhibitor_id` int NOT NULL AUTO_INCREMENT,
  `exhibitor_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `email_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `phone_no` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `company_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `company_description` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `company_addr` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `company_pin_code` int NOT NULL,
  `industry_id` int NOT NULL,
  `country_id` int DEFAULT NULL,
  `state_id` int DEFAULT NULL,
  PRIMARY KEY (`exhibitor_id`),
  KEY `industry_id` (`industry_id`),
  KEY `country_id` (`country_id`),
  KEY `state_id` (`state_id`),
  CONSTRAINT `exhibitor_ibfk_1` FOREIGN KEY (`industry_id`) REFERENCES `industry` (`industry_id`),
  CONSTRAINT `exhibitor_ibfk_2` FOREIGN KEY (`country_id`) REFERENCES `country` (`country_id`),
  CONSTRAINT `exhibitor_ibfk_3` FOREIGN KEY (`state_id`) REFERENCES `state` (`state_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table pyintern.exhibitor: ~3 rows (approximately)
DELETE FROM `exhibitor`;
/*!40000 ALTER TABLE `exhibitor` DISABLE KEYS */;
INSERT INTO `exhibitor` (`exhibitor_id`, `exhibitor_name`, `email_id`, `phone_no`, `company_name`, `company_description`, `company_addr`, `company_pin_code`, `industry_id`, `country_id`, `state_id`) VALUES
	(1, 'abc', 'abcgmail.com', '1234567890', 'Scam_company', 'Does scam calls', 'Mumbai', 401102, 1, 1, 2),
	(2, 'def', 'defgmail.com', '1234567890', 'Lifestyle', 'design clothes', 'Mumbai', 401100, 2, 1, 2),
	(4, 'xyz', 'pantaloons@gmail.com', '1234567890', 'Pantaloons', 'designer textiles', 'Mumbai', 401102, 1, 1, 3);
/*!40000 ALTER TABLE `exhibitor` ENABLE KEYS */;

-- Dumping structure for table pyintern.industry
CREATE TABLE IF NOT EXISTS `industry` (
  `industry_id` int NOT NULL AUTO_INCREMENT,
  `industry_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`industry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table pyintern.industry: ~2 rows (approximately)
DELETE FROM `industry`;
/*!40000 ALTER TABLE `industry` DISABLE KEYS */;
INSERT INTO `industry` (`industry_id`, `industry_name`) VALUES
	(1, 'food'),
	(2, 'textile');
/*!40000 ALTER TABLE `industry` ENABLE KEYS */;

-- Dumping structure for table pyintern.megaconsumercard
CREATE TABLE IF NOT EXISTS `megaconsumercard` (
  `card_id` int NOT NULL AUTO_INCREMENT,
  `spend_amt` int NOT NULL,
  `spend_date` datetime NOT NULL,
  `payment_mode` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `event_id` int DEFAULT NULL,
  `booking_id` int DEFAULT NULL,
  `visitor_id` int DEFAULT NULL,
  PRIMARY KEY (`card_id`),
  KEY `event_id` (`event_id`),
  KEY `booking_id` (`booking_id`),
  KEY `visitor_id` (`visitor_id`),
  CONSTRAINT `megaconsumercard_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `eventt` (`event_id`),
  CONSTRAINT `megaconsumercard_ibfk_2` FOREIGN KEY (`booking_id`) REFERENCES `booking` (`booking_id`),
  CONSTRAINT `megaconsumercard_ibfk_3` FOREIGN KEY (`visitor_id`) REFERENCES `visitor` (`visitor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table pyintern.megaconsumercard: ~2 rows (approximately)
DELETE FROM `megaconsumercard`;
/*!40000 ALTER TABLE `megaconsumercard` DISABLE KEYS */;
INSERT INTO `megaconsumercard` (`card_id`, `spend_amt`, `spend_date`, `payment_mode`, `event_id`, `booking_id`, `visitor_id`) VALUES
	(1, 3000, '2020-03-22 00:00:00', 'cash', 1, 1, 2),
	(2, 7000, '2020-03-27 00:00:00', 'online', 2, 2, 3);
/*!40000 ALTER TABLE `megaconsumercard` ENABLE KEYS */;

-- Dumping structure for table pyintern.stall
CREATE TABLE IF NOT EXISTS `stall` (
  `stall_id` int NOT NULL AUTO_INCREMENT,
  `stall_no` int NOT NULL,
  `stall_price` float NOT NULL,
  `stall_size` float DEFAULT NULL,
  `is_booked` varchar(1) NOT NULL,
  `event_id` int DEFAULT NULL,
  PRIMARY KEY (`stall_id`),
  KEY `event_id` (`event_id`),
  CONSTRAINT `stall_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `eventt` (`event_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table pyintern.stall: ~2 rows (approximately)
DELETE FROM `stall`;
/*!40000 ALTER TABLE `stall` DISABLE KEYS */;
INSERT INTO `stall` (`stall_id`, `stall_no`, `stall_price`, `stall_size`, `is_booked`, `event_id`) VALUES
	(1, 1, 10000, 1, 'y', 1),
	(2, 5, 20000, 2, 'y', 2);
/*!40000 ALTER TABLE `stall` ENABLE KEYS */;

-- Dumping structure for table pyintern.state
CREATE TABLE IF NOT EXISTS `state` (
  `state_id` int NOT NULL AUTO_INCREMENT,
  `state_name` varchar(255) DEFAULT NULL,
  `country_id` int DEFAULT NULL,
  PRIMARY KEY (`state_id`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `state_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`country_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table pyintern.state: ~5 rows (approximately)
DELETE FROM `state`;
/*!40000 ALTER TABLE `state` DISABLE KEYS */;
INSERT INTO `state` (`state_id`, `state_name`, `country_id`) VALUES
	(2, 'Maharashtra', 1),
	(3, 'West Bengal', 1),
	(4, 'Bihar', 1),
	(5, 'Victoria', 2),
	(6, 'Queensland', 2);
/*!40000 ALTER TABLE `state` ENABLE KEYS */;

-- Dumping structure for table pyintern.venue
CREATE TABLE IF NOT EXISTS `venue` (
  `venue_id` int NOT NULL AUTO_INCREMENT,
  `venue_city` varchar(255) DEFAULT NULL,
  `venue_addr` varchar(255) DEFAULT NULL,
  `country_id` int DEFAULT NULL,
  `state_id` int DEFAULT NULL,
  PRIMARY KEY (`venue_id`),
  KEY `country_id` (`country_id`),
  KEY `state_id` (`state_id`),
  CONSTRAINT `venue_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`country_id`),
  CONSTRAINT `venue_ibfk_2` FOREIGN KEY (`state_id`) REFERENCES `state` (`state_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table pyintern.venue: ~2 rows (approximately)
DELETE FROM `venue`;
/*!40000 ALTER TABLE `venue` DISABLE KEYS */;
INSERT INTO `venue` (`venue_id`, `venue_city`, `venue_addr`, `country_id`, `state_id`) VALUES
	(1, 'Mumbai', 'Ghatkopar', 1, 2),
	(2, 'Mumbai', 'Matunga', 1, 2);
/*!40000 ALTER TABLE `venue` ENABLE KEYS */;

-- Dumping structure for table pyintern.visitor
CREATE TABLE IF NOT EXISTS `visitor` (
  `visitor_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `addr` varchar(255) DEFAULT NULL,
  `pin_code` varchar(255) DEFAULT NULL,
  `mob_no` varchar(255) NOT NULL,
  `email_id` varchar(255) NOT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`visitor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Dumping data for table pyintern.visitor: ~4 rows (approximately)
DELETE FROM `visitor`;
/*!40000 ALTER TABLE `visitor` DISABLE KEYS */;
INSERT INTO `visitor` (`visitor_id`, `first_name`, `last_name`, `addr`, `pin_code`, `mob_no`, `email_id`, `date_of_birth`, `gender`) VALUES
	(1, 'Suraj', 'Prabhu', 'Mumbai', '400037', '8779798679', 'surajprabhu@somaiya.edu', '0000-00-00 00:00:00', 'M'),
	(2, 'Kanan', 'Sudhakaran', 'Mumbai', '400039', '87797982800', 'kannan.sudhakaran@somaiya.edu', '2017-06-15 09:49:21', 'M'),
	(3, 'Kanan', 'Sudhakaran', 'Mumbai', '400039', '87797982100', 'swabhav@somaiya.edu', '2020-01-01 00:00:00', 'M'),
	(4, 'Ramesh', 'Sudhakaran', 'Mumbai', '400077', '9329802800', 'ramesh_1.sudh@somaiya.edu', '2020-06-15 09:34:21', 'M');
/*!40000 ALTER TABLE `visitor` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
