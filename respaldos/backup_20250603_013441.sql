-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: proyecto
-- ------------------------------------------------------
-- Server version	8.0.30

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
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add backup',6,'add_backup'),(22,'Can change backup',6,'change_backup'),(23,'Can delete backup',6,'delete_backup'),(24,'Can view backup',6,'view_backup'),(25,'Can add categoria',7,'add_categoria'),(26,'Can change categoria',7,'change_categoria'),(27,'Can delete categoria',7,'delete_categoria'),(28,'Can view categoria',7,'view_categoria'),(29,'Can add configuracion respaldo',8,'add_configuracionrespaldo'),(30,'Can change configuracion respaldo',8,'change_configuracionrespaldo'),(31,'Can delete configuracion respaldo',8,'delete_configuracionrespaldo'),(32,'Can view configuracion respaldo',8,'view_configuracionrespaldo'),(33,'Can add pedido',9,'add_pedido'),(34,'Can change pedido',9,'change_pedido'),(35,'Can delete pedido',9,'delete_pedido'),(36,'Can view pedido',9,'view_pedido'),(37,'Can add proveedor',10,'add_proveedor'),(38,'Can change proveedor',10,'change_proveedor'),(39,'Can delete proveedor',10,'delete_proveedor'),(40,'Can view proveedor',10,'view_proveedor'),(41,'Can add user',11,'add_usuario'),(42,'Can change user',11,'change_usuario'),(43,'Can delete user',11,'delete_usuario'),(44,'Can view user',11,'view_usuario'),(45,'Can add producto',12,'add_producto'),(46,'Can change producto',12,'change_producto'),(47,'Can delete producto',12,'delete_producto'),(48,'Can view producto',12,'view_producto'),(49,'Can add detalle pedido',13,'add_detallepedido'),(50,'Can change detalle pedido',13,'change_detallepedido'),(51,'Can delete detalle pedido',13,'delete_detallepedido'),(52,'Can view detalle pedido',13,'view_detallepedido'),(53,'Can add venta',14,'add_venta'),(54,'Can change venta',14,'change_venta'),(55,'Can delete venta',14,'delete_venta'),(56,'Can view venta',14,'view_venta'),(57,'Can add detalle venta',15,'add_detalleventa'),(58,'Can change detalle venta',15,'change_detalleventa'),(59,'Can delete detalle venta',15,'delete_detalleventa'),(60,'Can view detalle venta',15,'view_detalleventa'),(61,'Can add actividad usuario',16,'add_actividadusuario'),(62,'Can change actividad usuario',16,'change_actividadusuario'),(63,'Can delete actividad usuario',16,'delete_actividadusuario'),(64,'Can view actividad usuario',16,'view_actividadusuario');
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(16,'pagina','actividadusuario'),(6,'pagina','backup'),(7,'pagina','categoria'),(8,'pagina','configuracionrespaldo'),(13,'pagina','detallepedido'),(15,'pagina','detalleventa'),(9,'pagina','pedido'),(12,'pagina','producto'),(10,'pagina','proveedor'),(11,'pagina','usuario'),(14,'pagina','venta'),(5,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-06-01 05:11:22.613271'),(2,'contenttypes','0002_remove_content_type_name','2025-06-01 05:11:22.665280'),(3,'auth','0001_initial','2025-06-01 05:11:22.832731'),(4,'auth','0002_alter_permission_name_max_length','2025-06-01 05:11:22.866547'),(5,'auth','0003_alter_user_email_max_length','2025-06-01 05:11:22.877324'),(6,'auth','0004_alter_user_username_opts','2025-06-01 05:11:22.883415'),(7,'auth','0005_alter_user_last_login_null','2025-06-01 05:11:22.887084'),(8,'auth','0006_require_contenttypes_0002','2025-06-01 05:11:22.888078'),(9,'auth','0007_alter_validators_add_error_messages','2025-06-01 05:11:22.891236'),(10,'auth','0008_alter_user_username_max_length','2025-06-01 05:11:22.895225'),(11,'auth','0009_alter_user_last_name_max_length','2025-06-01 05:11:22.899228'),(12,'auth','0010_alter_group_name_max_length','2025-06-01 05:11:22.911764'),(13,'auth','0011_update_proxy_permissions','2025-06-01 05:11:22.916786'),(14,'auth','0012_alter_user_first_name_max_length','2025-06-01 05:11:22.916786'),(15,'pagina','0001_initial','2025-06-01 05:11:23.456594'),(16,'admin','0001_initial','2025-06-01 05:11:23.539227'),(17,'admin','0002_logentry_remove_auto_add','2025-06-01 05:11:23.546227'),(18,'admin','0003_logentry_add_action_flag_choices','2025-06-01 05:11:23.552227'),(19,'pagina','0002_rename_cantidad_detalleventa_cantidad_vendida_and_more','2025-06-01 05:11:23.662558'),(20,'pagina','0003_alter_detalleventa_options_alter_venta_options_and_more','2025-06-01 05:11:23.789998'),(21,'pagina','0004_remove_proveedor_estado_alter_producto_id_and_more','2025-06-01 05:11:24.031675'),(22,'pagina','0005_alter_producto_id_alter_producto_table','2025-06-01 05:11:24.200975'),(23,'pagina','0006_actividadusuario','2025-06-01 05:11:24.242289'),(24,'sessions','0001_initial','2025-06-01 05:13:48.977122');
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
INSERT INTO `django_session` VALUES ('gnuk28ufivkgynge84ko26u9ozfu43m8','.eJxVjMsOwiAQRf-FtSHDowy4dO83EB6DVA0kpV0Z_12bdKHbe865L-bDtla_DVr8nNmZSXb63WJID2o7yPfQbp2n3tZljnxX-EEHv_ZMz8vh_h3UMOq3FlmLZPNkUQszFW1QIIHCUiw4iSGYHI0mXWKSCESEzgAZpVABJOfY-wPIxzcp:1uMF8Y:C_EKb_8B34bwQ61iAN7V2B8v9F8QUwrFpZ5ImJE1ZPg','2025-06-17 00:04:14.001442'),('jluspltkpkwdan7mjq2ji448yncsztvi','.eJxVjMsOwiAQRf-FtSEMD2lduu83kBkYpGogKe3K-O_apAvd3nPOfYmA21rC1nkJcxIXAeL0uxHGB9cdpDvWW5Ox1XWZSe6KPGiXU0v8vB7u30HBXr41Kc_Jo0EeGbUj5RSTzVHbgSIhgck2YrSDObND0Ow9ZJNVBkgZRxDvDxRkOQE:1uMGXp:m84rxCwJVo8rUFGeVtR6c6mq-wIsoXlQvkJcZDwJ2c8','2025-06-17 01:34:25.308198');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_actividadusuario`
--

DROP TABLE IF EXISTS `pagina_actividadusuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_actividadusuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo_actividad` varchar(50) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `fecha` datetime(6) NOT NULL,
  `icono` varchar(50) NOT NULL,
  `color` varchar(50) NOT NULL,
  `usuario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pagina_actividadusuario_usuario_id_8dc80073_fk_pagina_usuario_id` (`usuario_id`),
  CONSTRAINT `pagina_actividadusuario_usuario_id_8dc80073_fk_pagina_usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `pagina_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_actividadusuario`
--

LOCK TABLES `pagina_actividadusuario` WRITE;
/*!40000 ALTER TABLE `pagina_actividadusuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagina_actividadusuario` ENABLE KEYS */;
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
  `tipo` varchar(50) NOT NULL,
  `tamano` varchar(20) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `archivo` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_backup`
--

LOCK TABLES `pagina_backup` WRITE;
/*!40000 ALTER TABLE `pagina_backup` DISABLE KEYS */;
INSERT INTO `pagina_backup` VALUES (7,'2025-06-03 01:28:35.959654','Manual','19.44 MB','Completado','backup_20250603_012834.sql');
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_categoria`
--

LOCK TABLES `pagina_categoria` WRITE;
/*!40000 ALTER TABLE `pagina_categoria` DISABLE KEYS */;
INSERT INTO `pagina_categoria` VALUES (1,'aseo'),(3,'alimentos'),(4,'libros');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_configuracionrespaldo`
--

LOCK TABLES `pagina_configuracionrespaldo` WRITE;
/*!40000 ALTER TABLE `pagina_configuracionrespaldo` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagina_configuracionrespaldo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_detallepedido`
--

DROP TABLE IF EXISTS `pagina_detallepedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_detallepedido` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int unsigned NOT NULL,
  `pedido_id` bigint NOT NULL,
  `producto_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pagina_detallepedido_pedido_id_0a521758_fk_pagina_pedido_id` (`pedido_id`),
  KEY `pagina_detallepedido_producto_id_6811f4eb_fk` (`producto_id`),
  CONSTRAINT `pagina_detallepedido_pedido_id_0a521758_fk_pagina_pedido_id` FOREIGN KEY (`pedido_id`) REFERENCES `pagina_pedido` (`id`),
  CONSTRAINT `pagina_detallepedido_producto_id_6811f4eb_fk` FOREIGN KEY (`producto_id`) REFERENCES `pagina_producto` (`id`),
  CONSTRAINT `pagina_detallepedido_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_detallepedido`
--

LOCK TABLES `pagina_detallepedido` WRITE;
/*!40000 ALTER TABLE `pagina_detallepedido` DISABLE KEYS */;
INSERT INTO `pagina_detallepedido` VALUES (1,20,1,'72343434344'),(2,2,2,'72343434344'),(3,2,3,'72343434344'),(4,20,4,'7702212606904');
/*!40000 ALTER TABLE `pagina_detallepedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_detalleventa`
--

DROP TABLE IF EXISTS `pagina_detalleventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_detalleventa` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad_vendida` int unsigned NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `producto_id` varchar(50) NOT NULL,
  `venta_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pagina_detalleventa_venta_id_76e2e90d_fk_pagina_venta_id` (`venta_id`),
  KEY `pagina_detalleventa_producto_id_1197faec_fk` (`producto_id`),
  CONSTRAINT `pagina_detalleventa_producto_id_1197faec_fk` FOREIGN KEY (`producto_id`) REFERENCES `pagina_producto` (`id`),
  CONSTRAINT `pagina_detalleventa_venta_id_76e2e90d_fk_pagina_venta_id` FOREIGN KEY (`venta_id`) REFERENCES `pagina_venta` (`id`),
  CONSTRAINT `pagina_detalleventa_cantidad_vendida_6f7a8df1_check` CHECK ((`cantidad_vendida` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_detalleventa`
--

LOCK TABLES `pagina_detalleventa` WRITE;
/*!40000 ALTER TABLE `pagina_detalleventa` DISABLE KEYS */;
INSERT INTO `pagina_detalleventa` VALUES (1,4,3000.00,12000.00,'7702212606904',1);
/*!40000 ALTER TABLE `pagina_detalleventa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_pedido`
--

DROP TABLE IF EXISTS `pagina_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_pedido` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_pedido` datetime(6) NOT NULL,
  `fecha_entrega` date NOT NULL,
  `estado` varchar(20) NOT NULL,
  `proveedor_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pagina_pedido_proveedor_id_ed6f1983_fk_pagina_proveedor_id` (`proveedor_id`),
  CONSTRAINT `pagina_pedido_proveedor_id_ed6f1983_fk_pagina_proveedor_id` FOREIGN KEY (`proveedor_id`) REFERENCES `pagina_proveedor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_pedido`
--

LOCK TABLES `pagina_pedido` WRITE;
/*!40000 ALTER TABLE `pagina_pedido` DISABLE KEYS */;
INSERT INTO `pagina_pedido` VALUES (1,'2025-06-02 03:43:57.592463','2025-06-01','pendiente',1),(2,'2025-06-02 03:52:51.847991','2025-06-01','pendiente',1),(3,'2025-06-03 00:21:39.345467','2025-06-01','pendiente',1),(4,'2025-06-03 01:07:58.476939','2025-06-02','pendiente',1);
/*!40000 ALTER TABLE `pagina_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_producto`
--

DROP TABLE IF EXISTS `pagina_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_producto` (
  `id` varchar(50) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `iva` decimal(5,2) NOT NULL,
  `cantidad_producto` int NOT NULL,
  `fecha_vencimiento` date DEFAULT NULL,
  `imagen` varchar(100) DEFAULT NULL,
  `fecha_registro` datetime(6) NOT NULL,
  `categoria_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pagina_producto_categoria_id_dcb5dcb1_fk_pagina_categoria_id` (`categoria_id`),
  CONSTRAINT `pagina_producto_categoria_id_dcb5dcb1_fk_pagina_categoria_id` FOREIGN KEY (`categoria_id`) REFERENCES `pagina_categoria` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_producto`
--

LOCK TABLES `pagina_producto` WRITE;
/*!40000 ALTER TABLE `pagina_producto` DISABLE KEYS */;
INSERT INTO `pagina_producto` VALUES ('72343434344','fabuloso',4500.00,0.00,54,NULL,'productos/Fabuloso_W6i31mB.png','2025-06-01 06:49:28.784971',1),('7702212606904','cuadernos de 100 hojas',3000.00,0.00,66,NULL,'productos/agua_cristal_vF95gz9.png','2025-06-03 01:06:47.206095',4);
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_proveedor`
--

LOCK TABLES `pagina_proveedor` WRITE;
/*!40000 ALTER TABLE `pagina_proveedor` DISABLE KEYS */;
INSERT INTO `pagina_proveedor` VALUES (1,'105734213','babalu','babalu@gmail.com','3207644326','calle 14 N 14-11','2025-06-02 03:43:04.563809');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_usuario`
--

LOCK TABLES `pagina_usuario` WRITE;
/*!40000 ALTER TABLE `pagina_usuario` DISABLE KEYS */;
INSERT INTO `pagina_usuario` VALUES (1,'pbkdf2_sha256$870000$0kIkDZA6pPOACFmtC6Lzxb$tIUUXhmb0g8Lgg2rM5zk9rEaFXUza1s3JGpbYpSWyLs=','2025-06-03 01:21:51.696442',0,'yeisson','yeison','gonzalez',0,1,'2025-06-01 05:18:53.163551','CC','1057575428','administrador','yeissongonzalez2808@gmail.com','perfiles/Fabuloso.png','2025-06-01 05:18:53.992552'),(2,'pbkdf2_sha256$870000$kQy68TlsjgiMGsQMiKDjb4$wMklLNCUoBVJO8Jl1Hrb8z5mNNgYWZFBCMzk5v6/d5w=','2025-06-03 00:47:58.556135',0,'francisco','francisco','socha',0,1,'2025-06-01 05:20:45.713913','CC','1057575429','empleado','yeissosochi@gmail.com','','2025-06-01 05:20:46.605442'),(3,'pbkdf2_sha256$870000$qXnUsotY9jFHiQJtpaMqWN$f8B7d110r6jHa+ei9oKPXPDEgYtKu3XTtYI4rR/RPMk=','2025-06-03 01:17:33.776873',0,'yeissong','yeisson','gonza',0,1,'2025-06-03 00:38:01.125926','CC','1057575420','administrador','gonzalezsochayeissonfrancisco@gmail.com','','2025-06-03 00:38:02.023847');
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

--
-- Table structure for table `pagina_venta`
--

DROP TABLE IF EXISTS `pagina_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_venta` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_venta` datetime(6) NOT NULL,
  `vendedor_id` bigint NOT NULL,
  `total` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pagina_venta_vendedor_id_3fdb0a25_fk_pagina_usuario_id` (`vendedor_id`),
  CONSTRAINT `pagina_venta_vendedor_id_3fdb0a25_fk_pagina_usuario_id` FOREIGN KEY (`vendedor_id`) REFERENCES `pagina_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_venta`
--

LOCK TABLES `pagina_venta` WRITE;
/*!40000 ALTER TABLE `pagina_venta` DISABLE KEYS */;
INSERT INTO `pagina_venta` VALUES (1,'2025-06-03 01:09:37.996872',1,12000.00);
/*!40000 ALTER TABLE `pagina_venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-02 20:34:41
