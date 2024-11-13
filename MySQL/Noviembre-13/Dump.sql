-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: red_social
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `breeds`
--

DROP TABLE IF EXISTS `breeds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `breeds` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `specie_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_breeds_species1_idx` (`specie_id`),
  CONSTRAINT `fk_breeds_species1` FOREIGN KEY (`specie_id`) REFERENCES `species` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `breeds`
--

LOCK TABLES `breeds` WRITE;
/*!40000 ALTER TABLE `breeds` DISABLE KEYS */;
INSERT INTO `breeds` VALUES (1,'Labrador Retriever','2024-11-12 15:53:08','2024-11-12 15:53:08',1),(2,'Pastor Alemán','2024-11-12 15:53:08','2024-11-12 15:53:08',1),(3,'Bulldog Francés','2024-11-12 15:53:08','2024-11-12 15:53:08',1),(4,'Golden Retriever','2024-11-12 15:53:08','2024-11-12 15:53:08',1),(5,'Pug','2024-11-12 15:53:08','2024-11-12 15:53:08',1),(6,'Rottweiler','2024-11-12 15:53:08','2024-11-12 15:53:08',1),(7,'Beagle','2024-11-12 15:53:08','2024-11-12 15:53:08',1),(8,'Chihuahua','2024-11-12 15:53:08','2024-11-12 15:53:08',1),(9,'Shih Tzu','2024-11-12 15:53:08','2024-11-12 15:53:08',1),(10,'Boxer','2024-11-12 15:53:08','2024-11-12 15:53:08',1),(11,'Persa','2024-11-12 15:53:08','2024-11-12 15:53:08',2),(12,'Siamés','2024-11-12 15:53:08','2024-11-12 15:53:08',2),(13,'Maine Coon','2024-11-12 15:53:08','2024-11-12 15:53:08',2),(14,'Ragdoll','2024-11-12 15:53:08','2024-11-12 15:53:08',2),(15,'Bengalí','2024-11-12 15:53:08','2024-11-12 15:53:08',2),(16,'British Shorthair','2024-11-12 15:53:08','2024-11-12 15:53:08',2),(17,'Sphynx','2024-11-12 15:53:08','2024-11-12 15:53:08',2),(18,'Scottish Fold','2024-11-12 15:53:08','2024-11-12 15:53:08',2),(19,'Birmano','2024-11-12 15:53:08','2024-11-12 15:53:08',2),(20,'Azul Ruso','2024-11-12 15:53:08','2024-11-12 15:53:08',2),(21,'Árabe','2024-11-12 15:53:08','2024-11-12 15:53:08',3),(22,'Pura Sangre Inglés','2024-11-12 15:53:08','2024-11-12 15:53:08',3),(23,'Percherón','2024-11-12 15:53:08','2024-11-12 15:53:08',3),(24,'Appaloosa','2024-11-12 15:53:08','2024-11-12 15:53:08',3),(25,'Andaluz','2024-11-12 15:53:08','2024-11-12 15:53:08',3),(26,'Mustang','2024-11-12 15:53:08','2024-11-12 15:53:08',3),(27,'Frisón','2024-11-12 15:53:08','2024-11-12 15:53:08',3),(28,'Morgan','2024-11-12 15:53:08','2024-11-12 15:53:08',3),(29,'Clydesdale','2024-11-12 15:53:08','2024-11-12 15:53:08',3),(30,'Shetland','2024-11-12 15:53:08','2024-11-12 15:53:08',3),(31,'Holstein','2024-11-12 15:53:08','2024-11-12 15:53:08',4),(32,'Jersey','2024-11-12 15:53:08','2024-11-12 15:53:08',4),(33,'Hereford','2024-11-12 15:53:08','2024-11-12 15:53:08',4),(34,'Angus','2024-11-12 15:53:08','2024-11-12 15:53:08',4),(35,'Charolais','2024-11-12 15:53:08','2024-11-12 15:53:08',4),(36,'Limousin','2024-11-12 15:53:08','2024-11-12 15:53:08',4),(37,'Simental','2024-11-12 15:53:08','2024-11-12 15:53:08',4),(38,'Shorthorn','2024-11-12 15:53:08','2024-11-12 15:53:08',4),(39,'Brangus','2024-11-12 15:53:08','2024-11-12 15:53:08',4),(40,'Pardo Suizo','2024-11-12 15:53:08','2024-11-12 15:53:08',4),(41,'Plymouth Rock','2024-11-12 15:53:08','2024-11-12 15:53:08',5),(42,'Leghorn','2024-11-12 15:53:08','2024-11-12 15:53:08',5),(43,'Rhode Island Red','2024-11-12 15:53:08','2024-11-12 15:53:08',5),(44,'Orpington','2024-11-12 15:53:08','2024-11-12 15:53:08',5),(45,'Sussex','2024-11-12 15:53:08','2024-11-12 15:53:08',5),(46,'Brahma','2024-11-12 15:53:08','2024-11-12 15:53:08',5),(47,'Australorp','2024-11-12 15:53:08','2024-11-12 15:53:08',5),(48,'Cochin','2024-11-12 15:53:08','2024-11-12 15:53:08',5),(49,'Wyandotte','2024-11-12 15:53:08','2024-11-12 15:53:08',5),(50,'Barnevelder','2024-11-12 15:53:08','2024-11-12 15:53:08',5),(51,'Yorkshire','2024-11-12 15:53:08','2024-11-12 15:53:08',6),(52,'Duroc','2024-11-12 15:53:08','2024-11-12 15:53:08',6),(53,'Landrace','2024-11-12 15:53:08','2024-11-12 15:53:08',6),(54,'Berkshire','2024-11-12 15:53:08','2024-11-12 15:53:08',6),(55,'Hampshire','2024-11-12 15:53:08','2024-11-12 15:53:08',6),(56,'Chester White','2024-11-12 15:53:08','2024-11-12 15:53:08',6),(57,'Pietrain','2024-11-12 15:53:08','2024-11-12 15:53:08',6),(58,'Tamworth','2024-11-12 15:53:08','2024-11-12 15:53:08',6),(59,'Large Black','2024-11-12 15:53:08','2024-11-12 15:53:08',6),(60,'Poland China','2024-11-12 15:53:08','2024-11-12 15:53:08',6),(61,'Merino','2024-11-12 15:53:08','2024-11-12 15:53:08',7),(62,'Suffolk','2024-11-12 15:53:08','2024-11-12 15:53:08',7),(63,'Hampshire','2024-11-12 15:53:08','2024-11-12 15:53:08',7),(64,'Dorper','2024-11-12 15:53:08','2024-11-12 15:53:08',7),(65,'Katahdin','2024-11-12 15:53:08','2024-11-12 15:53:08',7),(66,'Romanov','2024-11-12 15:53:08','2024-11-12 15:53:08',7),(67,'Texel','2024-11-12 15:53:08','2024-11-12 15:53:08',7),(68,'Dorset','2024-11-12 15:53:08','2024-11-12 15:53:08',7),(69,'Awassi','2024-11-12 15:53:08','2024-11-12 15:53:08',7),(70,'Corriedale','2024-11-12 15:53:08','2024-11-12 15:53:08',7),(71,'Chinchilla','2024-11-12 15:53:08','2024-11-12 15:53:08',8),(72,'Hámster Dorado','2024-11-12 15:53:08','2024-11-12 15:53:08',8),(73,'Cobaya','2024-11-12 15:53:08','2024-11-12 15:53:08',8),(74,'Ratón Doméstico','2024-11-12 15:53:08','2024-11-12 15:53:08',8),(75,'Rata de Noruega','2024-11-12 15:53:08','2024-11-12 15:53:08',8),(76,'Jerbo','2024-11-12 15:53:08','2024-11-12 15:53:08',8),(77,'Degú','2024-11-12 15:53:08','2024-11-12 15:53:08',8),(78,'Conejillo de Indias','2024-11-12 15:53:08','2024-11-12 15:53:08',8),(79,'Ardilla de Richardson','2024-11-12 15:53:08','2024-11-12 15:53:08',8),(80,'Agutí','2024-11-12 15:53:08','2024-11-12 15:53:08',8),(81,'Goldfish','2024-11-12 15:53:08','2024-11-12 15:53:08',9),(82,'Betta','2024-11-12 15:53:08','2024-11-12 15:53:08',9),(83,'Guppy','2024-11-12 15:53:08','2024-11-12 15:53:08',9),(84,'Pez Ángel','2024-11-12 15:53:08','2024-11-12 15:53:08',9),(85,'Cíclido Africano','2024-11-12 15:53:08','2024-11-12 15:53:08',9),(86,'Molly','2024-11-12 15:53:08','2024-11-12 15:53:08',9),(87,'Tetra Neón','2024-11-12 15:53:08','2024-11-12 15:53:08',9),(88,'Oscar','2024-11-12 15:53:08','2024-11-12 15:53:08',9),(89,'Koi','2024-11-12 15:53:08','2024-11-12 15:53:08',9),(90,'Plecostomus','2024-11-12 15:53:08','2024-11-12 15:53:08',9),(91,'Llama','2024-11-12 15:53:08','2024-11-12 15:53:08',10),(92,'Alpaca','2024-11-12 15:53:08','2024-11-12 15:53:08',10),(93,'Guanaco','2024-11-12 15:53:08','2024-11-12 15:53:08',10),(94,'Vicuña','2024-11-12 15:53:08','2024-11-12 15:53:08',10),(95,'Dromedario','2024-11-12 15:53:08','2024-11-12 15:53:08',10),(96,'Camello Bactriano','2024-11-12 15:53:08','2024-11-12 15:53:08',10),(97,'Camello Árabe','2024-11-12 15:53:08','2024-11-12 15:53:08',10),(98,'Criollo','2024-11-12 15:53:08','2024-11-12 15:53:08',10),(99,'Tuwalu','2024-11-12 15:53:08','2024-11-12 15:53:08',10),(100,'Qashqai','2024-11-12 15:53:08','2024-11-12 15:53:08',10);
/*!40000 ALTER TABLE `breeds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `posts_id` int NOT NULL,
  `users_id` int NOT NULL,
  `content` text NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_posts_has_users_users2_idx` (`users_id`),
  KEY `fk_posts_has_users_posts2_idx` (`posts_id`),
  CONSTRAINT `fk_posts_has_users_posts2` FOREIGN KEY (`posts_id`) REFERENCES `posts` (`id`),
  CONSTRAINT `fk_posts_has_users_users2` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `connections`
--

DROP TABLE IF EXISTS `connections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `connections` (
  `user_id` int NOT NULL,
  `connection_id` int NOT NULL,
  PRIMARY KEY (`user_id`,`connection_id`),
  KEY `fk_users_has_users_users2_idx` (`connection_id`),
  KEY `fk_users_has_users_users1_idx` (`user_id`),
  CONSTRAINT `fk_users_has_users_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_users_has_users_users2` FOREIGN KEY (`connection_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `connections`
--

LOCK TABLES `connections` WRITE;
/*!40000 ALTER TABLE `connections` DISABLE KEYS */;
/*!40000 ALTER TABLE `connections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pets`
--

DROP TABLE IF EXISTS `pets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `birthdate` date NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `breed_id` int NOT NULL,
  `owner_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_pets_breeds_idx` (`breed_id`),
  KEY `fk_pets_users1_idx` (`owner_id`),
  CONSTRAINT `fk_pets_breeds` FOREIGN KEY (`breed_id`) REFERENCES `breeds` (`id`),
  CONSTRAINT `fk_pets_users1` FOREIGN KEY (`owner_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pets`
--

LOCK TABLES `pets` WRITE;
/*!40000 ALTER TABLE `pets` DISABLE KEYS */;
INSERT INTO `pets` VALUES (1,'Gandolfo','2019-03-15','2024-11-12 16:01:04','2024-11-12 16:01:04',71,1),(2,'Luna','2020-06-22','2024-11-12 16:01:04','2024-11-12 16:01:04',2,34),(3,'Rocky','2017-09-03','2024-11-12 16:01:04','2024-11-12 16:01:04',3,15),(4,'Bella','2018-11-17','2024-11-12 16:01:04','2024-11-12 16:01:04',4,12),(5,'Max','2021-01-11','2024-11-12 16:01:04','2024-11-12 16:01:04',5,25),(6,'Charlie','2019-08-29','2024-11-12 16:01:04','2024-11-12 16:01:04',6,18),(7,'Milo','2020-05-05','2024-11-12 16:01:04','2024-11-12 16:01:04',7,30),(8,'Daisy','2021-02-19','2024-11-12 16:01:04','2024-11-12 16:01:04',8,20),(9,'Lucy','2018-07-12','2024-11-12 16:01:04','2024-11-12 16:01:04',9,21),(10,'Cooper','2017-12-25','2024-11-12 16:01:04','2024-11-12 16:01:04',10,40),(11,'Buddy','2016-11-01','2024-11-12 16:01:04','2024-11-12 16:01:04',11,6),(12,'Rex','2021-04-10','2024-11-12 16:01:04','2024-11-12 16:01:04',12,33),(13,'Sadie','2019-02-27','2024-11-12 16:01:04','2024-11-12 16:01:04',13,8),(14,'Chester','2022-03-15','2024-11-12 16:01:04','2024-11-12 16:01:04',14,22),(15,'Rosie','2018-10-20','2024-11-12 16:01:04','2024-11-12 16:01:04',15,28),(16,'Zoe','2019-06-14','2024-11-12 16:01:04','2024-11-12 16:01:04',16,29),(17,'Toby','2020-02-08','2024-11-12 16:01:04','2024-11-12 16:01:04',17,35),(18,'Maggie','2017-07-03','2024-11-12 16:01:04','2024-11-12 16:01:04',18,36),(19,'Perry','2021-08-25','2024-11-12 16:01:04','2024-11-12 16:05:08',19,7),(20,'Nala','2020-12-19','2024-11-12 16:01:04','2024-11-12 16:01:04',20,11),(21,'Leo','2022-04-09','2024-11-12 16:01:04','2024-11-12 16:01:04',21,13),(22,'Jack','2016-12-04','2024-11-12 16:01:04','2024-11-12 16:01:04',22,38),(23,'Lilly','2018-01-23','2024-11-12 16:01:04','2024-11-12 16:01:04',23,4),(24,'Rusty','2019-07-30','2024-11-12 16:01:04','2024-11-12 16:01:04',24,5),(25,'Sammy','2021-10-12','2024-11-12 16:01:04','2024-11-12 16:01:04',25,39),(26,'Pepper','2020-11-14','2024-11-12 16:01:04','2024-11-12 16:01:04',26,32),(27,'Bailey','2017-04-25','2024-11-12 16:01:04','2024-11-12 16:01:04',27,41),(28,'Harley','2021-09-28','2024-11-12 16:01:04','2024-11-12 16:01:04',28,19),(29,'Misty','2018-04-18','2024-11-12 16:01:04','2024-11-12 16:01:04',29,9),(31,'Willow','2022-01-01','2024-11-12 16:01:04','2024-11-12 16:01:04',1,31),(32,'Charlie','2020-08-17','2024-11-12 16:01:04','2024-11-12 16:01:04',2,32),(33,'Shadow','2017-06-10','2024-11-12 16:01:04','2024-11-12 16:01:04',3,33),(34,'Cleo','2021-07-05','2024-11-12 16:01:04','2024-11-12 16:01:04',4,34),(35,'Bentley','2019-04-12','2024-11-12 16:01:04','2024-11-12 16:01:04',5,35),(36,'Gizmo','2020-03-08','2024-11-12 16:01:04','2024-11-12 16:01:04',6,36),(37,'Koda','2018-09-22','2024-11-12 16:01:04','2024-11-12 16:01:04',7,37),(38,'Maggie','2016-10-18','2024-11-12 16:01:04','2024-11-12 16:01:04',8,38),(39,'Ace','2021-02-25','2024-11-12 16:01:04','2024-11-12 16:01:04',9,39),(40,'Milo','2017-03-12','2024-11-12 16:01:04','2024-11-12 16:01:04',10,40),(41,'Ziggy','2020-10-14','2024-11-12 16:01:04','2024-11-12 16:01:04',11,41),(42,'Simba','2019-12-06','2024-11-12 16:01:04','2024-11-12 16:01:04',12,42),(43,'Nino','2021-05-03','2024-11-12 16:01:04','2024-11-12 16:01:04',13,43),(44,'Penny','2018-03-22','2024-11-12 16:01:04','2024-11-12 16:01:04',14,44),(45,'Buddy','2016-08-09','2024-11-12 16:01:04','2024-11-12 16:01:04',15,45),(46,'Duke','2019-01-20','2024-11-12 16:01:04','2024-11-12 16:01:04',16,46),(47,'Coco','2020-07-29','2024-11-12 16:01:04','2024-11-12 16:01:04',17,47),(48,'Jake','2018-12-13','2024-11-12 16:01:04','2024-11-12 16:01:04',18,48),(49,'Milo','2021-06-23','2024-11-12 16:01:04','2024-11-12 16:01:04',19,49);
/*!40000 ALTER TABLE `pets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post_pet_tags`
--

DROP TABLE IF EXISTS `post_pet_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `post_pet_tags` (
  `posts_id` int NOT NULL,
  `pets_id` int NOT NULL,
  PRIMARY KEY (`posts_id`,`pets_id`),
  KEY `fk_posts_has_pets_pets1_idx` (`pets_id`),
  KEY `fk_posts_has_pets_posts1_idx` (`posts_id`),
  CONSTRAINT `fk_posts_has_pets_pets1` FOREIGN KEY (`pets_id`) REFERENCES `pets` (`id`),
  CONSTRAINT `fk_posts_has_pets_posts1` FOREIGN KEY (`posts_id`) REFERENCES `posts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post_pet_tags`
--

LOCK TABLES `post_pet_tags` WRITE;
/*!40000 ALTER TABLE `post_pet_tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `post_pet_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` text NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `owner_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_posts_users1_idx` (`owner_id`),
  CONSTRAINT `fk_posts_users1` FOREIGN KEY (`owner_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reactions`
--

DROP TABLE IF EXISTS `reactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reactions` (
  `posts_id` int NOT NULL,
  `users_id` int NOT NULL,
  `type` enum('like','dislike','funny') NOT NULL,
  PRIMARY KEY (`posts_id`,`users_id`),
  KEY `fk_posts_has_users_users1_idx` (`users_id`),
  KEY `fk_posts_has_users_posts1_idx` (`posts_id`),
  CONSTRAINT `fk_posts_has_users_posts1` FOREIGN KEY (`posts_id`) REFERENCES `posts` (`id`),
  CONSTRAINT `fk_posts_has_users_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reactions`
--

LOCK TABLES `reactions` WRITE;
/*!40000 ALTER TABLE `reactions` DISABLE KEYS */;
/*!40000 ALTER TABLE `reactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `species`
--

DROP TABLE IF EXISTS `species`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `species` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `species`
--

LOCK TABLES `species` WRITE;
/*!40000 ALTER TABLE `species` DISABLE KEYS */;
INSERT INTO `species` VALUES (1,'Canino','2024-11-12 15:46:49','2024-11-12 15:48:32'),(2,'Felino','2024-11-12 15:46:49','2024-11-12 15:48:32'),(3,'Equino','2024-11-12 15:46:49','2024-11-12 15:47:13'),(4,'Bovino','2024-11-12 15:46:49','2024-11-12 15:46:49'),(5,'Ave','2024-11-12 15:46:49','2024-11-12 15:46:49'),(6,'Porcino','2024-11-12 15:46:49','2024-11-12 15:46:49'),(7,'Ovino','2024-11-12 15:46:49','2024-11-12 15:46:49'),(8,'Roedor','2024-11-12 15:46:49','2024-11-12 15:46:49'),(9,'Pez','2024-11-12 15:46:49','2024-11-12 15:46:49'),(10,'Camelido','2024-11-12 15:47:24','2024-11-12 15:47:24');
/*!40000 ALTER TABLE `species` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(125) NOT NULL,
  `lastname` varchar(125) NOT NULL,
  `email` varchar(125) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(250) NOT NULL,
  `address` text,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `referral_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_users_users1_idx` (`referral_id`),
  CONSTRAINT `fk_users_users1` FOREIGN KEY (`referral_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Nestor','Ribero','nestor@email.com','nribero','hola1234','Av siempre viva 1234','2024-11-12 15:21:48','2024-11-12 15:21:48',NULL),(2,'Ana','Gomez','ana.gomez1@email.com','agomez1','password123','Calle Luna 123','2024-11-12 15:27:45','2024-11-12 15:31:03',1),(3,'Luis','Martinez','luis.martinez@email.com','lmartinez','hola1234','Av Sol 456','2024-11-12 15:27:45','2024-11-12 15:31:03',1),(4,'Maria','Perez','maria.perez@email.com','mperez','segura567','Calle Verde 789','2024-11-12 15:27:45','2024-11-12 15:31:03',1),(5,'Jose','Ramirez','jose.ramirez@email.com','jramirez','clave345','Av Libertador 101','2024-11-12 15:27:45','2024-11-12 15:31:03',1),(6,'Elena','Lopez','elena.lopez@email.com','elopez','segura123','Calle Mar 202','2024-11-12 15:27:45','2024-11-12 15:31:03',1),(7,'Carlos','Torres','carlos.torres@email.com','ctorres','hola1234','Av Norte 303','2024-11-12 15:27:45','2024-11-12 15:31:03',1),(8,'Sofia','Diaz','sofia.diaz@email.com','sdiaz','segura789','Calle Sur 404','2024-11-12 15:27:45','2024-11-12 15:31:03',1),(9,'Miguel','Rivas','miguel.rivas@email.com','mrivas','clave678','Av Montaña 505','2024-11-12 15:27:45','2024-11-12 15:31:03',1),(10,'Julia','Jimenez','julia.jimenez@email.com','jjimenez','pass456','Calle Estrella 606','2024-11-12 15:27:45','2024-11-12 15:31:03',2),(11,'Pedro','Mendoza','pedro.mendoza@email.com','pmendoza','hola567','Av Del Sol 707','2024-11-12 15:27:45','2024-11-12 15:31:03',2),(12,'Claudia','Paredes','claudia.paredes@email.com','cparedes','clave789','Calle Del Mar 808','2024-11-12 15:27:45','2024-11-12 15:31:03',2),(13,'Diego','Soto','diego.soto@email.com','dsoto','segura234','Av Central 909','2024-11-12 15:27:45','2024-11-12 15:31:03',3),(14,'Lucia','Moreno','lucia.moreno@email.com','lmoreno','pass345','Calle Oeste 111','2024-11-12 15:27:45','2024-11-12 15:31:03',3),(15,'Raul','Vargas','raul.vargas@email.com','rvargas','hola123','Av Pacífico 222','2024-11-12 15:27:45','2024-11-12 15:31:03',4),(16,'Laura','Suarez','laura.suarez@email.com','lsuarez','clave567','Calle Pinos 333','2024-11-12 15:27:45','2024-11-12 15:31:04',2),(17,'Alberto','Castro','alberto.castro@email.com','acastro','segura678','Av Bosque 444','2024-11-12 15:27:45','2024-11-12 15:31:04',1),(18,'Patricia','Dominguez','patricia.dominguez@email.com','pdominguez','pass456','Calle Arena 555','2024-11-12 15:27:45','2024-11-12 15:31:04',2),(19,'Andres','Ortega','andres.ortega@email.com','aortega','hola234','Av Norte 666','2024-11-12 15:27:45','2024-11-12 15:31:04',5),(20,'Cristina','Garcia','cristina.garcia@email.com','cgarcia','clave123','Calle Azul 777','2024-11-12 15:27:45','2024-11-12 15:31:04',5),(21,'Fernando','Rivera','fernando.rivera@email.com','frivera','pass678','Av Luna 888','2024-11-12 15:27:45','2024-11-12 15:31:04',5),(22,'Monica','Blanco','monica.blanco@email.com','mblanco','hola456','Calle Sol 999','2024-11-12 15:27:45','2024-11-12 15:31:04',5),(23,'Adrian','Gonzalez','adrian.gonzalez@email.com','agonzalez','segura123','Av Rosa 1001','2024-11-12 15:27:45','2024-11-12 15:31:04',5),(24,'Nathalie','Serrano','nathalie.serrano@email.com','nserrano','clave234','Calle Amarillo 1010','2024-11-12 15:27:45','2024-11-12 15:31:04',1),(25,'Rafael','Peña','rafael.pena@email.com','rpena','pass789','Av Cristal 2020','2024-11-12 15:27:45','2024-11-12 15:31:04',1),(26,'Victoria','Alvarez','victoria.alvarez@email.com','valvarez','hola678','Calle Brisa 3030','2024-11-12 15:27:45','2024-11-12 15:31:04',1),(27,'Guillermo','Fuentes','guillermo.fuentes@email.com','gfuentes','segura456','Av Río 4040','2024-11-12 15:27:45','2024-11-12 15:31:04',2),(28,'Natalia','Barrera','natalia.barrera@email.com','nbarrera','clave567','Calle Lluvia 5050','2024-11-12 15:27:45','2024-11-12 15:27:45',NULL),(29,'Mauricio','Reyes','mauricio.reyes@email.com','mreyes','pass123','Av Camino 6060','2024-11-12 15:27:45','2024-11-12 15:31:04',10),(30,'Gloria','Paz','gloria.paz@email.com','gpaz','hola789','Calle Maravilla 7070','2024-11-12 15:27:45','2024-11-12 15:31:04',25),(31,'Alfredo','Correa','alfredo.correa@email.com','acorrea','segura234','Av Montaña 8080','2024-11-12 15:27:45','2024-11-12 15:31:04',10),(32,'Viviana','Sanchez','viviana.sanchez@email.com','vsanchez','pass345','Calle Arboleda 9090','2024-11-12 15:27:45','2024-11-12 15:31:04',25),(33,'Gustavo','Mejia','gustavo.mejia@email.com','gmejia','hola234','Av Ceiba 10101','2024-11-12 15:27:45','2024-11-12 15:31:04',25),(34,'Daniela','Fernandez','daniela.fernandez@email.com','dfernandez','clave678','Calle Sol 11111','2024-11-12 15:27:45','2024-11-12 15:31:04',10),(35,'Sebastian','Ochoa','sebastian.ochoa@email.com','sochoa','segura123','Av Brisa 12121','2024-11-12 15:27:45','2024-11-12 15:27:45',NULL),(36,'Paola','Rincon','paola.rincon@email.com','princon','pass789','Calle Azul 13131','2024-11-12 15:27:45','2024-11-12 15:31:04',10),(37,'Rodrigo','Leal','rodrigo.leal@email.com','rleal','hola567','Av Bosque 14141','2024-11-12 15:27:45','2024-11-12 15:31:04',25),(38,'Carolina','Nieto','carolina.nieto@email.com','cnieto','clave345','Calle Montaña 15151','2024-11-12 15:27:45','2024-11-12 15:31:04',10),(39,'Ricardo','Benitez','ricardo.benitez@email.com','rbenitez','segura456','Av Estrella 16161','2024-11-12 15:27:45','2024-11-12 15:27:45',NULL),(40,'Esteban','Lara','esteban.lara@email.com','elara','pass567','Calle Del Mar 17171','2024-11-12 15:27:45','2024-11-12 15:31:04',25),(41,'Lorena','Munoz','lorena.munoz@email.com','lmunoz','hola678','Av Sol 18181','2024-11-12 15:27:45','2024-11-12 15:31:04',25),(42,'Sergio','Guerrero','sergio.guerrero@email.com','sguerrero','clave789','Calle Lluvia 19191','2024-11-12 15:27:45','2024-11-12 15:31:04',10),(43,'Alicia','Rojas','alicia.rojas@email.com','arojas','segura123','Av Río 20202','2024-11-12 15:27:45','2024-11-12 15:27:45',NULL),(44,'Ivan','Hernandez','ivan.hernandez@email.com','ihernandez','pass123','Calle Mar 21212','2024-11-12 15:27:45','2024-11-12 15:27:45',NULL),(45,'Jessica','Flores','jessica.flores@email.com','jflores','hola345','Av Cielo 22222','2024-11-12 15:27:45','2024-11-12 15:31:04',10),(46,'Cesar','Quintero','cesar.quintero@email.com','cquintero','clave456','Calle Camino 23232','2024-11-12 15:27:45','2024-11-12 15:27:45',NULL),(47,'Marcela','Campos','marcela.campos@email.com','mcampos','segura234','Av Brisa 24242','2024-11-12 15:27:45','2024-11-12 15:27:45',NULL),(48,'Angel','Salazar','angel.salazar@email.com','asalazar','pass678','Calle Estrella 25252','2024-11-12 15:27:45','2024-11-12 15:31:04',25),(49,'Fabiana','Acosta','fabiana.acosta@email.com','facosta','hola234','Av Sol 26262','2024-11-12 15:27:45','2024-11-12 15:27:45',NULL),(50,'Juan','Molina','juan.molina@email.com','jmolina','clave567','Calle Luna 27272','2024-11-12 15:27:45','2024-11-12 15:31:04',25);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-13 16:49:26
