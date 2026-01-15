-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: blood_donner_database
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `doctor_details`
--

DROP TABLE IF EXISTS `doctor_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_details` (
  `Name_of_Doctor` varchar(100) NOT NULL,
  `Doctor_Specification` varchar(200) NOT NULL,
  `Experience` varchar(100) NOT NULL,
  `Contact_Details` varchar(100) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `CLASSIFY` varchar(100) NOT NULL,
  `Age` int NOT NULL,
  `Doc_Id` int NOT NULL,
  UNIQUE KEY `Doc_Id` (`Doc_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_details`
--

LOCK TABLES `doctor_details` WRITE;
/*!40000 ALTER TABLE `doctor_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `doctor_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donnation_bank_info`
--

DROP TABLE IF EXISTS `donnation_bank_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donnation_bank_info` (
  `Name_Of_Bank` varchar(100) NOT NULL,
  `Postal_Code` int NOT NULL,
  `Contact_Number` varchar(100) NOT NULL,
  `Address_Of_Bank` varchar(100) NOT NULL,
  `LANDMARK` varchar(100) NOT NULL,
  `State` varchar(100) NOT NULL,
  `District` varchar(100) NOT NULL,
  `Number_of_Blood_Types` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donnation_bank_info`
--

LOCK TABLES `donnation_bank_info` WRITE;
/*!40000 ALTER TABLE `donnation_bank_info` DISABLE KEYS */;
/*!40000 ALTER TABLE `donnation_bank_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medical_details`
--

DROP TABLE IF EXISTS `medical_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medical_details` (
  `Name` varchar(100) NOT NULL,
  `Allergies` varchar(100) NOT NULL,
  `Height` varchar(100) NOT NULL,
  `Weight` varchar(100) NOT NULL,
  `Blood_Type` varchar(100) NOT NULL,
  `Any_Severe_Medical_History` varchar(100) NOT NULL,
  `Any_Disease` varchar(100) NOT NULL,
  `Any_Disease_Related_To_Blood` varchar(100) NOT NULL,
  `Any_Vaccination` varchar(100) NOT NULL,
  `Any_Medication_Going_On` varchar(100) NOT NULL,
  `Age` int NOT NULL,
  `User_Id` int NOT NULL,
  UNIQUE KEY `User_Id` (`User_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medical_details`
--

LOCK TABLES `medical_details` WRITE;
/*!40000 ALTER TABLE `medical_details` DISABLE KEYS */;
INSERT INTO `medical_details` VALUES ('Black Adam','N/A','180','100','B+VE','N/A','N/A','N/A','N/A','N/A',35,4428498),('Dekku','N/A','170','89','B+VE','N/A','N/A','N/A','N/A','N/A',19,9512534);
/*!40000 ALTER TABLE `medical_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_details`
--

DROP TABLE IF EXISTS `personal_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personal_details` (
  `Name` varchar(100) NOT NULL,
  `Age` int NOT NULL,
  `Phone_Number` varchar(100) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `State` varchar(28) NOT NULL,
  `District` varchar(59) NOT NULL,
  `Email_Id` varchar(120) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `User_Id` int NOT NULL,
  UNIQUE KEY `Email_Id` (`Email_Id`),
  UNIQUE KEY `Password` (`Password`),
  UNIQUE KEY `User_Id` (`User_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_details`
--

LOCK TABLES `personal_details` WRITE;
/*!40000 ALTER TABLE `personal_details` DISABLE KEYS */;
INSERT INTO `personal_details` VALUES ('black adam',35,'98530-45830','Paul_Street 92','USA','New York','adam@gmail.com','adam@123',4428498),('deku',19,'9392047','MHA1','Tokyo','Shihuya','deku@gmail.com','allmight@123',9512534),('luffy',21,'75034590','Grand_line','New_World','Land_Of_Wano','luffy@gmail.com','meat123',109082);
/*!40000 ALTER TABLE `personal_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-26 18:48:45
