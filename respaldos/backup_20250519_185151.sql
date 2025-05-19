-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: proyecto
-- ------------------------------------------------------
-- Server version	9.1.0

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add categoria',6,'add_categoria'),(22,'Can change categoria',6,'change_categoria'),(23,'Can delete categoria',6,'delete_categoria'),(24,'Can view categoria',6,'view_categoria'),(25,'Can add proveedor',7,'add_proveedor'),(26,'Can change proveedor',7,'change_proveedor'),(27,'Can delete proveedor',7,'delete_proveedor'),(28,'Can view proveedor',7,'view_proveedor'),(29,'Can add user',8,'add_usuario'),(30,'Can change user',8,'change_usuario'),(31,'Can delete user',8,'delete_usuario'),(32,'Can view user',8,'view_usuario'),(33,'Can add producto',9,'add_producto'),(34,'Can change producto',9,'change_producto'),(35,'Can delete producto',9,'delete_producto'),(36,'Can view producto',9,'view_producto'),(37,'Can add configuracion respaldo',10,'add_configuracionrespaldo'),(38,'Can change configuracion respaldo',10,'change_configuracionrespaldo'),(39,'Can delete configuracion respaldo',10,'delete_configuracionrespaldo'),(40,'Can view configuracion respaldo',10,'view_configuracionrespaldo'),(41,'Can add backup',11,'add_backup'),(42,'Can change backup',11,'change_backup'),(43,'Can delete backup',11,'delete_backup'),(44,'Can view backup',11,'view_backup');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_pagina_usuario_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_pagina_usuario_id` FOREIGN KEY (`user_id`) REFERENCES `pagina_usuario` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(11,'pagina','backup'),(6,'pagina','categoria'),(10,'pagina','configuracionrespaldo'),(9,'pagina','producto'),(7,'pagina','proveedor'),(8,'pagina','usuario'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-05-14 17:47:18.145607'),(2,'contenttypes','0002_remove_content_type_name','2025-05-14 17:47:18.235055'),(3,'auth','0001_initial','2025-05-14 17:47:18.704858'),(4,'auth','0002_alter_permission_name_max_length','2025-05-14 17:47:18.869260'),(5,'auth','0003_alter_user_email_max_length','2025-05-14 17:47:18.884966'),(6,'auth','0004_alter_user_username_opts','2025-05-14 17:47:18.901468'),(7,'auth','0005_alter_user_last_login_null','2025-05-14 17:47:18.913867'),(8,'auth','0006_require_contenttypes_0002','2025-05-14 17:47:18.917910'),(9,'auth','0007_alter_validators_add_error_messages','2025-05-14 17:47:18.930268'),(10,'auth','0008_alter_user_username_max_length','2025-05-14 17:47:18.943609'),(11,'auth','0009_alter_user_last_name_max_length','2025-05-14 17:47:18.953669'),(12,'auth','0010_alter_group_name_max_length','2025-05-14 17:47:18.995374'),(13,'auth','0011_update_proxy_permissions','2025-05-14 17:47:19.011928'),(14,'auth','0012_alter_user_first_name_max_length','2025-05-14 17:47:19.023720'),(15,'pagina','0001_initial','2025-05-14 17:47:19.791498'),(16,'admin','0001_initial','2025-05-14 17:47:20.087336'),(17,'admin','0002_logentry_remove_auto_add','2025-05-14 17:47:20.110994'),(18,'admin','0003_logentry_add_action_flag_choices','2025-05-14 17:47:20.136343'),(19,'sessions','0001_initial','2025-05-14 17:47:20.216986'),(20,'pagina','0002_configuracionrespaldo','2025-05-16 22:01:59.553159'),(21,'pagina','0003_backup','2025-05-19 18:14:51.000738'),(22,'pagina','0004_alter_backup_estado_alter_backup_tipo','2025-05-19 18:17:09.412953');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('d88lgmxy1d0po1dyukjddbcyfmmvs7j7','.eJzVkT9PwzAQxb_KyUuXKHKSpjHdqMTIwtpU0cW-NC6pXdkOA4jvjlO1FTAggSoBkqf783vP915Yg2Pom9GTa7RiS5ax5H2tRflIZmqoHZqtTaU1wek2nUbSU9en91bRsDrNfgD06Pu43XGiVsx51eVSYJ4JrMqCCiyUqDgtFqTKLBMlCmqR8upGZVSKTnDeVZIKySfonrzHLfmIW69r1jQ7b825WrMEeAJ5mUDNVugJVHwYrAdHPuDoUCFI6xzJgHsy4bhSs5ptEvga90D-gIOysCVDkWN_yLmarTmfRm6d7PWTnYju7NBYIHPMKNr8BdKdc9YBDqdTuQtvCSZ-D2bP-tDpgWagfZQIUbLThtRfEPgU9iWf78f9_29xJYENe30DrNhvlg:1uH5aV:CRfQ0ri_LTBJgaCsPNC7YwOuffW8lyMAOJ37imD39CY','2025-06-02 18:51:47.047807'),('qsuolyh0fdn56tzanjvuckz4rhpt519s','.eJxVjEEOwiAQRe_C2pABpIwu3XsGMjCDVA1NSrsy3l2bdKHb_977LxVpXWpcu8xxZHVWRh1-t0T5IW0DfKd2m3Se2jKPSW-K3mnX14nledndv4NKvX7rAiIJjxCKzUjWIAXvxJFjDCDDIOyNQU8oicSGExvxWBCghCwug3p_AO6JODY:1uG3eS:cko9Kl-LpT91Ed46_rZIPHfEA5vVuS24-qbjIvJaiaU','2025-05-30 22:35:36.403156');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_backup`
--

DROP TABLE IF EXISTS `pagina_backup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_backup` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha` datetime(6) NOT NULL,
  `tipo` varchar(20) NOT NULL,
  `tamano` varchar(20) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `archivo` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_backup`
--

LOCK TABLES `pagina_backup` WRITE;
/*!40000 ALTER TABLE `pagina_backup` DISABLE KEYS */;
INSERT INTO `pagina_backup` VALUES (2,'2025-05-19 18:42:54.846775','Manual','0.02 MB','Completado','backup_20250519_184254.sql');
/*!40000 ALTER TABLE `pagina_backup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_categoria`
--

DROP TABLE IF EXISTS `pagina_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_categoria`
--

LOCK TABLES `pagina_categoria` WRITE;
/*!40000 ALTER TABLE `pagina_categoria` DISABLE KEYS */;
INSERT INTO `pagina_categoria` VALUES (1,'Aseo');
/*!40000 ALTER TABLE `pagina_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_configuracionrespaldo`
--

DROP TABLE IF EXISTS `pagina_configuracionrespaldo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_configuracionrespaldo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `frecuencia` varchar(10) NOT NULL,
  `hora` time(6) NOT NULL,
  `cantidad` int unsigned NOT NULL,
  `actualizado` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `pagina_configuracionrespaldo_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_configuracionrespaldo`
--

LOCK TABLES `pagina_configuracionrespaldo` WRITE;
/*!40000 ALTER TABLE `pagina_configuracionrespaldo` DISABLE KEYS */;
INSERT INTO `pagina_configuracionrespaldo` VALUES (1,'diario','02:00:00.000000',5,'2025-05-16 22:03:26.198103');
/*!40000 ALTER TABLE `pagina_configuracionrespaldo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_producto`
--

DROP TABLE IF EXISTS `pagina_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `iva` decimal(5,2) NOT NULL,
  `cantidad_entrada` int NOT NULL,
  `cantidad_salida` int NOT NULL,
  `fecha_vencimiento` date DEFAULT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `fecha_registro` datetime(6) NOT NULL,
  `categoria_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pagina_producto_categoria_id_dcb5dcb1_fk_pagina_categoria_id` (`categoria_id`),
  CONSTRAINT `pagina_producto_categoria_id_dcb5dcb1_fk_pagina_categoria_id` FOREIGN KEY (`categoria_id`) REFERENCES `pagina_categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_producto`
--

LOCK TABLES `pagina_producto` WRITE;
/*!40000 ALTER TABLE `pagina_producto` DISABLE KEYS */;
INSERT INTO `pagina_producto` VALUES (1,'Papel higienico',2500.00,0.00,50,0,'2025-05-14','','2025-05-14 18:22:50.806163',1);
/*!40000 ALTER TABLE `pagina_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_proveedor`
--

DROP TABLE IF EXISTS `pagina_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_proveedor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nit_proveedor` varchar(20) NOT NULL,
  `empresa` varchar(100) NOT NULL,
  `correo` varchar(254) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `fecha_registro` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nit_proveedor` (`nit_proveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_proveedor`
--

LOCK TABLES `pagina_proveedor` WRITE;
/*!40000 ALTER TABLE `pagina_proveedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagina_proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_usuario`
--

DROP TABLE IF EXISTS `pagina_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_usuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `tipo_documento` varchar(2) NOT NULL,
  `numero_documento` varchar(20) NOT NULL,
  `rol` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `imagen_perfil` varchar(100) DEFAULT NULL,
  `fecha_registro` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `numero_documento` (`numero_documento`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_usuario`
--

LOCK TABLES `pagina_usuario` WRITE;
/*!40000 ALTER TABLE `pagina_usuario` DISABLE KEYS */;
INSERT INTO `pagina_usuario` VALUES (1,'pbkdf2_sha256$870000$sRCwzGapfty1f0XbQLZIqt$3d7V3UaPfQHWjajqrsnWoj/n1z5yiEKVmDoDNZdmkBo=','2025-05-19 18:41:30.371454',0,'Javier','Javier','Gomez',0,1,'2025-05-14 18:20:44.680256','CC','7367356','empleado','jxvierg05@gmail.com','perfiles/narutopeuqeno_WGksddT.gif','2025-05-14 18:20:53.510843');
/*!40000 ALTER TABLE `pagina_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_usuario_groups`
--

DROP TABLE IF EXISTS `pagina_usuario_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_usuario_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pagina_usuario_groups_usuario_id_group_id_98ccf565_uniq` (`usuario_id`,`group_id`),
  KEY `pagina_usuario_groups_group_id_d0157da6_fk_auth_group_id` (`group_id`),
  CONSTRAINT `pagina_usuario_groups_group_id_d0157da6_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `pagina_usuario_groups_usuario_id_74c5405c_fk_pagina_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `pagina_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_usuario_groups`
--

LOCK TABLES `pagina_usuario_groups` WRITE;
/*!40000 ALTER TABLE `pagina_usuario_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagina_usuario_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_usuario_user_permissions`
--

DROP TABLE IF EXISTS `pagina_usuario_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_usuario_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pagina_usuario_user_perm_usuario_id_permission_id_744904c9_uniq` (`usuario_id`,`permission_id`),
  KEY `pagina_usuario_user__permission_id_1075808b_fk_auth_perm` (`permission_id`),
  CONSTRAINT `pagina_usuario_user__permission_id_1075808b_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `pagina_usuario_user__usuario_id_ccea10b5_fk_pagina_us` FOREIGN KEY (`usuario_id`) REFERENCES `pagina_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_usuario_user_permissions`
--

LOCK TABLES `pagina_usuario_user_permissions` WRITE;
/*!40000 ALTER TABLE `pagina_usuario_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagina_usuario_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-19 13:51:51
