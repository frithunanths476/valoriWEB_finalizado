-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: valori
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `ID_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(254) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `senha` varchar(254) DEFAULT NULL,
  PRIMARY KEY (`ID_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (4,'João','joao123@gmail.com','123'),(5,'Soso','soso@gmail.com','123456789'),(6,'João2','joao123@gmail.com','123'),(7,'GG','gg@gmail.com','8624'),(8,'Qwerty','qwerty@gmail.com','987654'),(9,'Matheus','matheus@gmail.com','$2b$12$MEZ1N7VaM4LknQHYMNmccOhJPUR4PZuxIwsqQU5DiDkvlxOoSTCEK'),(10,'Mirko','Mirko@gmail.com','$2b$12$HiX0TUtyAFAj4u84w9V64egicSIig5VdgWh7D4E88LPBiYFjz0l4K'),(11,'Jão','jao@gmail.com','$2b$12$axoRidjzCOZ0oU9RdNW9vOAmFbl4f9hvsa8fV3t.FR0a2PCK.3xCu'),(12,'Gustavo Bolsonaro','GB22@Gmail.com','$2b$12$KOo.Kn5aZjjuGSu3rmHsGOgjnQj8Ph4XGjAPYTF397Jryejv0WAYC'),(13,'Gustavo Bolsonaro','GB23@Gmail.com','$2b$12$sqQ8tsorlYGgcdPNeSBC6edKfwMzff8DjCloSyaWu.Q1KIfnHalnW'),(14,'Gustavo Bolsonaro','GB24@Gmail.com','$2b$12$DuSmTEmNKS9.3FLXRf5DzOPxIcqHBy9DEPNHTLGWA.0H.P/QuJIhK'),(15,'Jão','jao2@gmail.com','$2b$12$kPtrfiWX94aFKci9zH18x.dDsmRVaxbRVhCMtg4jpQxOrxXEs9rGa');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-15 16:34:36
