-- -------------------------------------------------------------
-- TablePlus 6.0.0(550)
--
-- https://tableplus.com/
--
-- Database: button
-- Generation Time: 2024-05-17 16:45:37.4080
-- -------------------------------------------------------------


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `auth_group_permissions`;
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

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `datas_planpart`;
CREATE TABLE `datas_planpart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `delete_flag` varchar(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` bigint NOT NULL,
  `part_id` bigint DEFAULT NULL,
  `updated_by_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `datas_planpart_created_by_id_4b30d113_fk_landingPa` (`created_by_id`),
  KEY `datas_planpart_part_id_74d16be5_fk_order_bommaster_id` (`part_id`),
  KEY `datas_planpart_updated_by_id_4d285633_fk_landingPa` (`updated_by_id`),
  CONSTRAINT `datas_planpart_created_by_id_4b30d113_fk_landingPa` FOREIGN KEY (`created_by_id`) REFERENCES `landingPage_usermaster` (`id`),
  CONSTRAINT `datas_planpart_part_id_74d16be5_fk_order_bommaster_id` FOREIGN KEY (`part_id`) REFERENCES `order_bommaster` (`id`),
  CONSTRAINT `datas_planpart_updated_by_id_4d285633_fk_landingPa` FOREIGN KEY (`updated_by_id`) REFERENCES `landingPage_usermaster` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `datas_plantation`;
CREATE TABLE `datas_plantation` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(50) NOT NULL,
  `name` varchar(100) NOT NULL,
  `owner` varchar(100) NOT NULL,
  `delete_flag` varchar(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `bom_id` bigint DEFAULT NULL,
  `created_by_id` bigint NOT NULL,
  `updated_by_id` bigint NOT NULL,
  `part_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `c_code` (`code`),
  KEY `datas_plantation_bom_id_b679176c_fk_order_bommaster_id` (`bom_id`),
  KEY `datas_plantation_created_by_id_e082041a_fk_landingPa` (`created_by_id`),
  KEY `datas_plantation_updated_by_id_85a57078_fk_landingPa` (`updated_by_id`),
  KEY `datas_plantation_part_id_9645bdd0_fk_datas_planpart_id` (`part_id`),
  CONSTRAINT `datas_plantation_bom_id_b679176c_fk_order_bommaster_id` FOREIGN KEY (`bom_id`) REFERENCES `order_bommaster` (`id`),
  CONSTRAINT `datas_plantation_created_by_id_e082041a_fk_landingPa` FOREIGN KEY (`created_by_id`) REFERENCES `landingPage_usermaster` (`id`),
  CONSTRAINT `datas_plantation_part_id_9645bdd0_fk_datas_planpart_id` FOREIGN KEY (`part_id`) REFERENCES `datas_planpart` (`id`),
  CONSTRAINT `datas_plantation_updated_by_id_85a57078_fk_landingPa` FOREIGN KEY (`updated_by_id`) REFERENCES `landingPage_usermaster` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `landingPage_customermaster`;
CREATE TABLE `landingPage_customermaster` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(255) NOT NULL,
  `licensee_no` varchar(255) NOT NULL,
  `owner_name` varchar(255) NOT NULL,
  `bus_con` varchar(255) DEFAULT NULL,
  `bus_event` varchar(255) DEFAULT NULL,
  `postal_code` varchar(255) DEFAULT NULL,
  `addr` varchar(255) DEFAULT NULL,
  `office_tel` varchar(255) DEFAULT NULL,
  `office_fax` varchar(255) DEFAULT NULL,
  `office_email` varchar(254) DEFAULT NULL,
  `charge_name` varchar(255) DEFAULT NULL,
  `charge_tel` varchar(255) DEFAULT NULL,
  `charge_pos` varchar(255) DEFAULT NULL,
  `etc` longtext,
  `cus_type` varchar(255) DEFAULT NULL,
  `delete_flag` varchar(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id_id` bigint NOT NULL,
  `updated_by_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `landingPage_customer_created_by_id_id_09d300ce_fk_landingPa` (`created_by_id_id`),
  KEY `landingPage_customer_updated_by_id_id_c6538de5_fk_landingPa` (`updated_by_id_id`),
  CONSTRAINT `landingPage_customer_created_by_id_id_09d300ce_fk_landingPa` FOREIGN KEY (`created_by_id_id`) REFERENCES `landingPage_usermaster` (`id`),
  CONSTRAINT `landingPage_customer_updated_by_id_id_c6538de5_fk_landingPa` FOREIGN KEY (`updated_by_id_id`) REFERENCES `landingPage_usermaster` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `landingPage_usermaster`;
CREATE TABLE `landingPage_usermaster` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `join_date` date DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `tel` varchar(255) DEFAULT NULL,
  `fax` varchar(255) DEFAULT NULL,
  `signature` varchar(100) DEFAULT NULL,
  `delete_flag` varchar(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `custom_id` bigint DEFAULT NULL,
  `created_by_id` int NOT NULL,
  `updated_by_id` int NOT NULL,
  `is_master` varchar(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `landingPage_usermast_custom_id_eb61d390_fk_landingPa` (`custom_id`),
  KEY `landingPage_usermaster_created_by_id_24f959c8_fk_auth_user_id` (`created_by_id`),
  KEY `landingPage_usermaster_updated_by_id_e806b989_fk_auth_user_id` (`updated_by_id`),
  CONSTRAINT `landingPage_usermast_custom_id_eb61d390_fk_landingPa` FOREIGN KEY (`custom_id`) REFERENCES `landingPage_customermaster` (`id`),
  CONSTRAINT `landingPage_usermaster_created_by_id_24f959c8_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `landingPage_usermaster_updated_by_id_e806b989_fk_auth_user_id` FOREIGN KEY (`updated_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `landingPage_usermaster_user_id_56903ac6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `order_basicbom`;
CREATE TABLE `order_basicbom` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `level` int NOT NULL,
  `delete_flag` varchar(1) NOT NULL,
  `item_id` bigint NOT NULL,
  `parent_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_basicbom_item_id_e561689f_fk_order_itemmaster_id` (`item_id`),
  KEY `order_basicbom_parent_id_34eaf93f_fk` (`parent_id`),
  CONSTRAINT `order_basicbom_item_id_e561689f_fk_order_itemmaster_id` FOREIGN KEY (`item_id`) REFERENCES `order_itemmaster` (`id`),
  CONSTRAINT `order_basicbom_parent_id_34eaf93f_fk` FOREIGN KEY (`parent_id`) REFERENCES `order_basicbom` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `order_bommaster`;
CREATE TABLE `order_bommaster` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `level` int NOT NULL,
  `part` varchar(255) NOT NULL,
  `tax` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `delete_flag` varchar(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int NOT NULL,
  `item_id` bigint DEFAULT NULL,
  `op_id` bigint DEFAULT NULL,
  `parent_id` bigint DEFAULT NULL,
  `updated_by_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_bommaster_created_by_id_c267922b_fk_auth_user_id` (`created_by_id`),
  KEY `order_bommaster_updated_by_id_90e365cb_fk_auth_user_id` (`updated_by_id`),
  KEY `order_bommaster_parent_id_8d6252b4_fk_order_bommaster_id` (`parent_id`),
  KEY `order_bommaster_item_id_658521c4_fk_order_itemmaster_id` (`item_id`),
  KEY `order_bommaster_op_id_4574b1eb_fk_order_orderproduct_id` (`op_id`),
  CONSTRAINT `order_bommaster_created_by_id_c267922b_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `order_bommaster_item_id_658521c4_fk_order_itemmaster_id` FOREIGN KEY (`item_id`) REFERENCES `order_itemmaster` (`id`),
  CONSTRAINT `order_bommaster_op_id_4574b1eb_fk_order_orderproduct_id` FOREIGN KEY (`op_id`) REFERENCES `order_orderproduct` (`id`),
  CONSTRAINT `order_bommaster_parent_id_8d6252b4_fk_order_bommaster_id` FOREIGN KEY (`parent_id`) REFERENCES `order_bommaster` (`id`),
  CONSTRAINT `order_bommaster_updated_by_id_90e365cb_fk_auth_user_id` FOREIGN KEY (`updated_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `order_itemmaster`;
CREATE TABLE `order_itemmaster` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `specification` longtext,
  `model` longtext,
  `brand` varchar(255) DEFAULT NULL,
  `level` varchar(255) NOT NULL,
  `standard_price` int DEFAULT NULL,
  `delete_flag` varchar(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `created_by_id` int NOT NULL,
  `updated_by_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `item_code` (`code`),
  KEY `order_itemmaster_created_by_id_ba5427e2_fk_auth_user_id` (`created_by_id`),
  KEY `order_itemmaster_updated_by_id_f4abd200_fk_auth_user_id` (`updated_by_id`),
  CONSTRAINT `order_itemmaster_created_by_id_ba5427e2_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `order_itemmaster_updated_by_id_f4abd200_fk_auth_user_id` FOREIGN KEY (`updated_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `order_ordermaster`;
CREATE TABLE `order_ordermaster` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `so_no` varchar(255) NOT NULL,
  `order_date` date NOT NULL,
  `cnt` int NOT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `comment` longtext NOT NULL,
  `delete_flag` varchar(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `client_id` bigint DEFAULT NULL,
  `created_by_id` int DEFAULT NULL,
  `updated_by_id` int DEFAULT NULL,
  `status` varchar(1) NOT NULL,
  `place` varchar(255) NOT NULL,
  `tax` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_ordermaster_client_id_0470f257_fk_landingPa` (`client_id`),
  KEY `order_ordermaster_created_by_id_b4d9dcfb_fk_auth_user_id` (`created_by_id`),
  KEY `order_ordermaster_updated_by_id_cd4f4032_fk_auth_user_id` (`updated_by_id`),
  CONSTRAINT `order_ordermaster_client_id_0470f257_fk_landingPa` FOREIGN KEY (`client_id`) REFERENCES `landingPage_usermaster` (`id`),
  CONSTRAINT `order_ordermaster_created_by_id_b4d9dcfb_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `order_ordermaster_updated_by_id_cd4f4032_fk_auth_user_id` FOREIGN KEY (`updated_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `order_orderproduct`;
CREATE TABLE `order_orderproduct` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `unique_no` varchar(255) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `delivery_date` datetime(6) DEFAULT NULL,
  `order_cnt` int DEFAULT NULL,
  `delivery_addr` varchar(255) DEFAULT NULL,
  `request_note` longtext,
  `status` varchar(255) DEFAULT NULL,
  `delete_flag` varchar(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `bom_id` bigint DEFAULT NULL,
  `created_by_id` int NOT NULL,
  `order_id` bigint DEFAULT NULL,
  `updated_by_id` int NOT NULL,
  `crops` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `order_orderproduct_created_by_id_8d597183_fk_auth_user_id` (`created_by_id`),
  KEY `order_orderproduct_updated_by_id_b4a2de43_fk_auth_user_id` (`updated_by_id`),
  KEY `order_orderproduct_bom_id_dbf7270c_fk_order_bommaster_id` (`bom_id`),
  KEY `order_orderproduct_order_id_18dae3b0_fk_order_ordermaster_id` (`order_id`),
  CONSTRAINT `order_orderproduct_bom_id_dbf7270c_fk_order_bommaster_id` FOREIGN KEY (`bom_id`) REFERENCES `order_bommaster` (`id`),
  CONSTRAINT `order_orderproduct_created_by_id_8d597183_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `order_orderproduct_order_id_18dae3b0_fk_order_ordermaster_id` FOREIGN KEY (`order_id`) REFERENCES `order_ordermaster` (`id`),
  CONSTRAINT `order_orderproduct_updated_by_id_b4a2de43_fk_auth_user_id` FOREIGN KEY (`updated_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add customer master', 7, 'add_customermaster'),
(26, 'Can change customer master', 7, 'change_customermaster'),
(27, 'Can delete customer master', 7, 'delete_customermaster'),
(28, 'Can view customer master', 7, 'view_customermaster'),
(29, 'Can add user master', 8, 'add_usermaster'),
(30, 'Can change user master', 8, 'change_usermaster'),
(31, 'Can delete user master', 8, 'delete_usermaster'),
(32, 'Can view user master', 8, 'view_usermaster'),
(33, 'Can add plan part', 9, 'add_planpart'),
(34, 'Can change plan part', 9, 'change_planpart'),
(35, 'Can delete plan part', 9, 'delete_planpart'),
(36, 'Can view plan part', 9, 'view_planpart'),
(37, 'Can add plantation', 10, 'add_plantation'),
(38, 'Can change plantation', 10, 'change_plantation'),
(39, 'Can delete plantation', 10, 'delete_plantation'),
(40, 'Can view plantation', 10, 'view_plantation'),
(41, 'Can add basic bom', 11, 'add_basicbom'),
(42, 'Can change basic bom', 11, 'change_basicbom'),
(43, 'Can delete basic bom', 11, 'delete_basicbom'),
(44, 'Can view basic bom', 11, 'view_basicbom'),
(45, 'Can add bom master', 12, 'add_bommaster'),
(46, 'Can change bom master', 12, 'change_bommaster'),
(47, 'Can delete bom master', 12, 'delete_bommaster'),
(48, 'Can view bom master', 12, 'view_bommaster'),
(49, 'Can add order master', 13, 'add_ordermaster'),
(50, 'Can change order master', 13, 'change_ordermaster'),
(51, 'Can delete order master', 13, 'delete_ordermaster'),
(52, 'Can view order master', 13, 'view_ordermaster'),
(53, 'Can add order product', 14, 'add_orderproduct'),
(54, 'Can change order product', 14, 'change_orderproduct'),
(55, 'Can delete order product', 14, 'delete_orderproduct'),
(56, 'Can view order product', 14, 'view_orderproduct'),
(57, 'Can add item master', 15, 'add_itemmaster'),
(58, 'Can change item master', 15, 'change_itemmaster'),
(59, 'Can delete item master', 15, 'delete_itemmaster'),
(60, 'Can view item master', 15, 'view_itemmaster');

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$GJELmeB5n7tfKwgGUxY2jI$DZX6FXb47MlSdxlmzqeBHjIAoWJ6urnWWrYW+tnTG3k=', '2024-05-17 05:38:16.984562', 0, 'seoulsoft', '', '', 'seoulsoft@seoul-soft.com', 0, 1, '2024-05-16 07:21:22.561414');

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'landingPage', 'customermaster'),
(8, 'landingPage', 'usermaster'),
(9, 'datas', 'planpart'),
(10, 'datas', 'plantation'),
(11, 'order', 'basicbom'),
(12, 'order', 'bommaster'),
(13, 'order', 'ordermaster'),
(14, 'order', 'orderproduct'),
(15, 'order', 'itemmaster');

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-05-16 06:41:41.875581'),
(2, 'auth', '0001_initial', '2024-05-16 06:41:41.998070'),
(3, 'admin', '0001_initial', '2024-05-16 06:41:42.029050'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-05-16 06:41:42.032354'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-05-16 06:41:42.036163'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-05-16 06:41:42.054762'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-05-16 06:41:42.068428'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-05-16 06:41:42.076064'),
(9, 'auth', '0004_alter_user_username_opts', '2024-05-16 06:41:42.078753'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-05-16 06:41:42.094480'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-05-16 06:41:42.095010'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-05-16 06:41:42.097775'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-05-16 06:41:42.112564'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-05-16 06:41:42.126025'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-05-16 06:41:42.132275'),
(16, 'auth', '0011_update_proxy_permissions', '2024-05-16 06:41:42.136103'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-05-16 06:41:42.148703'),
(18, 'order', '0001_initial', '2024-05-16 06:41:42.365408'),
(19, 'order', '0002_alter_itemmaster_id', '2024-05-16 06:41:42.425520'),
(20, 'order', '0003_rename_child_id_bommaster_child_and_more', '2024-05-16 06:41:43.349970'),
(21, 'landingPage', '0001_initial', '2024-05-16 06:41:43.476944'),
(22, 'landingPage', '0002_remove_usermaster_password_and_more', '2024-05-16 06:41:43.504521'),
(23, 'landingPage', '0003_remove_usermaster_is_master_and_more', '2024-05-16 06:41:43.892513'),
(24, 'landingPage', '0004_remove_usermaster_email', '2024-05-16 06:41:43.903277'),
(25, 'landingPage', '0005_remove_usermaster_custom_id_usermaster_custom', '2024-05-16 06:41:43.949967'),
(26, 'order', '0004_alter_ordermaster_client', '2024-05-16 06:41:43.993194'),
(27, 'order', '0005_ordermaster_order_status_alter_bommaster_created_at_and_more', '2024-05-16 06:41:44.041023'),
(28, 'order', '0006_ordermaster_order_delivery_place', '2024-05-16 06:41:44.058035'),
(29, 'order', '0007_alter_ordermaster_order_date', '2024-05-16 06:41:44.077595'),
(30, 'order', '0008_remove_bommaster_child', '2024-05-16 06:41:44.106378'),
(31, 'order', '0009_alter_bommaster_parent', '2024-05-16 06:41:44.145618'),
(32, 'order', '0010_alter_orderproduct_bom', '2024-05-16 06:41:44.185335'),
(33, 'order', '0011_alter_bommaster_parent', '2024-05-16 06:41:44.191162'),
(34, 'order', '0012_alter_bommaster_op_alter_bommaster_parent', '2024-05-16 06:41:44.239864'),
(35, 'order', '0013_alter_orderproduct_bom', '2024-05-16 06:41:44.245528'),
(36, 'landingPage', '0006_remove_usermaster_created_by_id_and_more', '2024-05-16 06:41:44.348362'),
(37, 'landingPage', '0007_alter_usermaster_created_by_and_more', '2024-05-16 06:41:44.435052'),
(38, 'order', '0014_alter_bommaster_parent_alter_ordermaster_client_and_more', '2024-05-16 06:41:44.574308'),
(39, 'order', '0015_alter_bommaster_op', '2024-05-16 06:41:44.622737'),
(40, 'order', '0016_alter_bommaster_item_alter_bommaster_op_and_more', '2024-05-16 06:41:44.738550'),
(41, 'order', '0017_rename_code_name_basicbom_code_and_more', '2024-05-16 06:41:44.912231'),
(42, 'order', '0018_rename_cnt_orderproduct_order_cnt', '2024-05-16 06:41:44.923209'),
(43, 'order', '0019_ordermaster_tax', '2024-05-16 06:41:44.934097'),
(44, 'order', '0020_ordermaster_total', '2024-05-16 06:41:44.947447'),
(45, 'order', '0021_remove_basicbom_child', '2024-05-16 06:41:44.970356'),
(46, 'landingPage', '0008_rename_user_code_usermaster_code_and_more', '2024-05-16 06:41:45.038845'),
(47, 'datas', '0001_initial', '2024-05-16 06:41:45.114259'),
(48, 'datas', '0002_rename_p_name_planpart_name_and_more', '2024-05-16 06:41:45.141521'),
(49, 'datas', '0003_plantation_part', '2024-05-16 06:41:45.160398'),
(50, 'sessions', '0001_initial', '2024-05-16 06:41:45.168310');

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('l06dbez8yn4o3b9v7xrrnusf4hdcfum3', '.eJxVjMsOgjAUBf-la9PQC4XWpXu_obmvWtRAQmFl_HclYaHbMzPnZRJua0lb1SWNYs7GmdPvRsgPnXYgd5xus-V5WpeR7K7Yg1Z7nUWfl8P9OyhYy7fugNA3itwBawSHrXiOEoIjiJm1aRmGLB4oaE8EFL30xMKa3RBIzPsDBDE5SQ:1s7VQY:TvW7Rm77_BrgnoFNWPbZnZ7c2aWAPGPPRtkX-GQNPlY', '2024-05-30 07:21:22.862918'),
('smhftutck3xq3399bd2gqfw7w6s43trq', '.eJxVjMsOgjAUBf-la9PQC4XWpXu_obmvWtRAQmFl_HclYaHbMzPnZRJua0lb1SWNYs7GmdPvRsgPnXYgd5xus-V5WpeR7K7Yg1Z7nUWfl8P9OyhYy7fugNA3itwBawSHrXiOEoIjiJm1aRmGLB4oaE8EFL30xMKa3RBIzPsDBDE5SQ:1s7qIK:b9-rPNjb5ot3H9vVYsbyyZ4C1ZsnmB3vrI7QHNkZXKE', '2024-05-31 05:38:16.989058'),
('z3rb9z9jgo4iqxjew74yxmga61roqtk6', '.eJxVjMsOgjAUBf-la9PQC4XWpXu_obmvWtRAQmFl_HclYaHbMzPnZRJua0lb1SWNYs7GmdPvRsgPnXYgd5xus-V5WpeR7K7Yg1Z7nUWfl8P9OyhYy7fugNA3itwBawSHrXiOEoIjiJm1aRmGLB4oaE8EFL30xMKa3RBIzPsDBDE5SQ:1s7lml:aPiLeQcKajNwERawz3kJVfffm819q8FQcDAeEHA5kaU', '2024-05-31 00:49:23.889356');

INSERT INTO `landingPage_usermaster` (`id`, `code`, `name`, `join_date`, `address`, `tel`, `fax`, `signature`, `delete_flag`, `created_at`, `updated_at`, `user_id`, `custom_id`, `created_by_id`, `updated_by_id`, `is_master`) VALUES
(1, '134-87-18556', '서울소프트', NULL, NULL, NULL, NULL, '', 'N', '2024-05-16 07:21:22.850282', '2024-05-16 07:21:22.850298', 1, NULL, 1, 1, '');

INSERT INTO `order_bommaster` (`id`, `level`, `part`, `tax`, `total`, `delete_flag`, `created_at`, `updated_at`, `created_by_id`, `item_id`, `op_id`, `parent_id`, `updated_by_id`) VALUES
(1, 0, '컨테이너명', 50000.00, 500000.00, 'N', '2024-05-17 00:52:31.898545', '2024-05-17 00:52:31.898594', 1, 1, 1, NULL, 1),
(2, 1, '모니터링', 2500.00, 25000.00, 'N', '2024-05-17 00:52:42.281498', '2024-05-17 00:52:42.281553', 1, 2, 2, 1, 1),
(3, 1, '컨트롤러', 2500.00, 25000.00, 'Y', '2024-05-17 00:52:50.507239', '2024-05-17 00:52:50.507291', 1, 3, 3, 1, 1),
(4, 0, '컨테이너명', 5000.00, 50000.00, 'N', '2024-05-17 00:53:03.755264', '2024-05-17 00:53:03.755283', 1, 1, 4, NULL, 1),
(5, 2, '추적 센서', 1250.00, 12500.00, 'N', '2024-05-17 00:57:34.230317', '2024-05-17 00:57:34.230355', 1, 4, 5, 2, 1),
(6, 2, '습도 센서', 2000.00, 20000.00, 'Y', '2024-05-17 00:57:40.248466', '2024-05-17 00:57:40.248512', 1, 5, 6, 3, 1),
(7, 0, '컨테이너명', 60000.00, 600000.00, 'N', '2024-05-17 04:30:25.958579', '2024-05-17 04:30:25.958621', 1, 1, 7, NULL, 1),
(8, 1, '컨트롤러', 500.00, 5000.00, 'N', '2024-05-17 04:30:38.671477', '2024-05-17 04:30:38.671514', 1, 3, 8, 7, 1),
(9, 0, '컨테이너명', 50000.00, 500000.00, 'N', '2024-05-17 04:51:58.475976', '2024-05-17 04:51:58.476016', 1, 1, 9, NULL, 1),
(10, 1, '컨트롤러', 500.00, 5000.00, 'N', '2024-05-17 04:52:10.610095', '2024-05-17 04:52:10.610129', 1, 3, 10, 9, 1),
(11, 2, 'duvbba', 270.00, 2700.00, 'N', '2024-05-17 04:52:27.626331', '2024-05-17 04:52:27.626375', 1, 10, 11, 10, 1),
(12, 2, '그린', 270.00, 2700.00, 'Y', '2024-05-17 04:52:46.239996', '2024-05-17 04:52:46.240037', 1, 14, 12, 10, 1);

INSERT INTO `order_itemmaster` (`id`, `code`, `name`, `type`, `specification`, `model`, `brand`, `level`, `standard_price`, `delete_flag`, `created_at`, `updated_at`, `created_by_id`, `updated_by_id`) VALUES
(1, '100-001', '컨테이너명', '컨테이너 ', 'level1', '', '', '1', 50000, 'N', '2024-05-17 00:49:49.247081', '2024-05-17 00:56:30.331839', 1, 1),
(2, '110-002', '모니터링', '모니터링', '', '', '', '2', 5000, 'N', '2024-05-17 00:51:19.741141', '2024-05-17 00:56:18.886737', 1, 1),
(3, '110-001', '컨트롤러', '컨트롤러', '', '', '', '2', 5000, 'N', '2024-05-17 00:51:53.560182', '2024-05-17 00:56:05.795082', 1, 1),
(4, '115-001', '추적 센서', '온도조절', '', '', '', '3', 2500, 'N', '2024-05-17 00:55:15.882972', '2024-05-17 00:55:15.883006', 1, 1),
(5, '115-002', '습도 센서', '습도 조절', '', '', '', '3', 4000, 'N', '2024-05-17 00:55:40.685711', '2024-05-17 00:55:40.685747', 1, 1),
(6, '115-003', '카메라', '카메라', '', '', '', '3', 5000, 'N', '2024-05-17 02:12:32.758328', '2024-05-17 02:12:32.758364', 1, 1),
(8, '115-004', 'diom', '온도센서', '', '', '', '3', 3900, 'N', '2024-05-17 02:13:34.405072', '2024-05-17 02:13:34.405098', 1, 1),
(10, '115-006', 'opui', '온도센서', '', '', '', '3', 2700, 'N', '2024-05-17 02:15:32.478627', '2024-05-17 02:15:32.478659', 1, 1),
(12, '115-007', 'dddv', '온도센서', '', '', '', '3', 3500, 'N', '2024-05-17 02:17:16.066357', '2024-05-17 02:25:25.264560', 1, 1),
(14, '115-008', 'duvbba', '온도센서', '', '', '', '3', 2700, 'N', '2024-05-17 02:18:10.299182', '2024-05-17 02:18:10.299211', 1, 1),
(15, '115-009', 'hello', '습도 조절', '', '', '', '3', 2700, 'N', '2024-05-17 02:18:32.324668', '2024-05-17 02:18:32.324749', 1, 1),
(16, '501-116', '헬로우', '모니터링', '', '', '', '3', 4000, 'N', '2024-05-17 02:19:27.053875', '2024-05-17 02:19:27.053906', 1, 1),
(17, '501-117', '옐로우', '모니터링', '', '', '', '3', 5700, 'N', '2024-05-17 02:20:15.970224', '2024-05-17 02:20:15.970254', 1, 1),
(18, '501-118', '그린', '색상', '', '', '', '3', 7500, 'N', '2024-05-17 02:20:59.595480', '2024-05-17 02:20:59.595533', 1, 1),
(20, '501-119', '블루', '색상', '', '', '', '3', 3500, 'N', '2024-05-17 02:21:22.993822', '2024-05-17 02:25:31.326347', 1, 1),
(21, '501-120', '바이올렛', '색상', '', '', '', '3', 9000, 'N', '2024-05-17 02:25:05.302069', '2024-05-17 02:25:17.234598', 1, 1);

INSERT INTO `order_ordermaster` (`id`, `so_no`, `order_date`, `cnt`, `price`, `comment`, `delete_flag`, `created_at`, `updated_at`, `client_id`, `created_by_id`, `updated_by_id`, `status`, `place`, `tax`, `total`) VALUES
(1, 'BF240517', '2024-05-15', 10, 50000.00, '', 'Y', '2024-05-17 00:52:15.797779', '2024-05-17 00:52:15.797818', 1, 1, 1, '1', '', 50000.00, 500000.00),
(2, 'BF240517', '2024-05-02', 20, 10000.00, '', 'N', '2024-05-17 02:27:54.554908', '2024-05-17 02:27:54.554921', 1, 1, 1, '1', '', 20000.00, 200000.00),
(3, 'BF240517', '2024-05-02', 20, 10000.00, '', 'N', '2024-05-17 02:27:54.554386', '2024-05-17 02:27:54.554406', 1, 1, 1, '1', '', 20000.00, 200000.00),
(4, 'BF240517', '2024-05-02', 20, 10000.00, '', 'N', '2024-05-17 02:28:18.957122', '2024-05-17 02:28:18.957136', 1, 1, 1, '1', '', 20000.00, 200000.00),
(5, 'BF240517', '2024-05-02', 20, 10000.00, '', 'N', '2024-05-17 02:28:19.712111', '2024-05-17 02:28:19.712140', 1, 1, 1, '1', '', 20000.00, 200000.00),
(6, 'BF240517', '2024-05-02', 20, 10000.00, '', 'N', '2024-05-17 02:28:20.127003', '2024-05-17 02:28:20.127419', 1, 1, 1, '1', '', 20000.00, 200000.00),
(7, 'BF240517', '2024-05-06', 20, 15000.00, '', 'N', '2024-05-17 02:28:36.924127', '2024-05-17 02:28:36.924154', 1, 1, 1, '1', '', 30000.00, 300000.00),
(8, 'BF240517', '2024-05-06', 20, 15000.00, '', 'N', '2024-05-17 02:28:36.954296', '2024-05-17 02:28:36.954335', 1, 1, 1, '1', '', 30000.00, 300000.00),
(9, 'BF240517', '2024-05-07', 100, 2000.00, '', 'N', '2024-05-17 02:28:55.310697', '2024-05-17 02:28:55.310724', 1, 1, 1, '1', '', 20000.00, 200000.00),
(10, 'BF240517', '2024-05-07', 100, 2000.00, '', 'N', '2024-05-17 02:28:55.314503', '2024-05-17 02:28:55.314536', 1, 1, 1, '1', '', 20000.00, 200000.00),
(11, 'BF240517', '2024-04-29', 1, 23300.00, '', 'N', '2024-05-17 02:30:02.457593', '2024-05-17 02:30:02.457617', 1, 1, 1, '1', '', 2330.00, 23300.00),
(12, 'BF240517', '2024-05-02', 10, 900.00, '', 'N', '2024-05-17 02:30:17.506865', '2024-05-17 02:30:17.506885', 1, 1, 1, '1', '', 900.00, 9000.00),
(13, 'BF240517', '2024-05-14', 23, 1000.00, '', 'N', '2024-05-17 02:31:26.358435', '2024-05-17 02:31:26.358456', 1, 1, 1, '1', '', 2300.00, 23000.00),
(14, 'BF240517', '2024-05-14', 24, 1000.00, '', 'N', '2024-05-17 02:31:34.434099', '2024-05-17 02:31:34.434125', 1, 1, 1, '1', '', 2300.00, 23000.00),
(15, 'BF240517', '2024-05-14', 24, 1000.00, '', 'N', '2024-05-17 02:31:35.304562', '2024-05-17 02:31:35.304590', 1, 1, 1, '1', '', 2300.00, 23000.00),
(16, 'BF240517', '2024-05-14', 12, 10000.00, '', 'N', '2024-05-17 02:35:21.163366', '2024-05-17 02:35:21.163401', 1, 1, 1, '1', '', 12000.00, 120000.00),
(17, 'BF240517', '2024-05-08', 10, 15000.00, '', 'N', '2024-05-17 02:35:50.268797', '2024-05-17 02:35:50.268819', 1, 1, 1, '1', '', 15000.00, 150000.00),
(18, 'BF240517', '2024-05-01', 12, 15000.00, '', 'N', '2024-05-17 02:36:08.941341', '2024-05-17 02:36:08.941389', 1, 1, 1, '1', '', 18000.00, 180000.00),
(19, 'BF240517', '2024-05-06', 23, 1000.00, '', 'N', '2024-05-17 02:36:55.195827', '2024-05-17 02:36:55.195845', 1, 1, 1, '1', '', 2300.00, 23000.00),
(20, 'BF240517', '2024-05-08', 23, 100.00, '', 'Y', '2024-05-17 02:42:02.038562', '2024-05-17 02:42:02.038582', 1, 1, 1, '1', '', 230.00, 2300.00),
(21, 'BF240517', '2024-05-01', 1, 10000.00, '', 'Y', '2024-05-17 02:43:04.535070', '2024-05-17 02:43:04.535100', 1, 1, 1, '1', '', 1000.00, 10000.00),
(22, 'BF240517', '2024-05-01', 23, 3000.00, '', 'Y', '2024-05-17 02:44:13.840136', '2024-05-17 02:44:13.840162', 1, 1, 1, '1', '', 3000.00, 30000.00);

INSERT INTO `order_orderproduct` (`id`, `unique_no`, `product_name`, `delivery_date`, `order_cnt`, `delivery_addr`, `request_note`, `status`, `delete_flag`, `created_at`, `updated_at`, `bom_id`, `created_by_id`, `order_id`, `updated_by_id`, `crops`) VALUES
(1, 'e7f14876-6f90-440a-9e2d-e6b1fcfda696', '컨테이너명', '2024-05-17 00:52:31.889936', 10, 'HCM', 'Test', '1', 'N', '2024-05-17 00:52:31.894700', '2024-05-17 00:52:31.894728', 1, 1, 1, 1, NULL),
(2, '743ae4a0-f37f-4bf4-9165-6f9505e9c9b4', '모니터링', '2024-05-17 00:52:42.275714', 5, 'HCM', 'Test', '1', 'N', '2024-05-17 00:52:42.278270', '2024-05-17 00:52:42.278287', 2, 1, 1, 1, NULL),
(3, '5d051ab5-ed19-40ff-b174-d8e134c61f5b', '컨트롤러', '2024-05-17 00:52:50.502786', 5, 'HCM', 'Test', '1', 'Y', '2024-05-17 00:52:50.504798', '2024-05-17 00:52:50.504817', 3, 1, 1, 1, NULL),
(4, '14e33830-8f67-4c90-9800-3a262cd54b10', '컨테이너명', '2024-05-17 00:53:03.751674', 1, 'HCM', 'Test', '1', 'N', '2024-05-17 00:53:03.753651', '2024-05-17 00:53:03.753665', 4, 1, 1, 1, NULL),
(5, 'ff0fcbe3-99a3-4bc2-8652-2864e01002e3', '추적 센서', '2024-05-17 00:57:34.225434', 5, 'HCM', 'Test', '1', 'N', '2024-05-17 00:57:34.227420', '2024-05-17 00:57:34.227437', 5, 1, 1, 1, NULL),
(6, '0b874be8-83ec-475b-81d5-4dee1db3ab82', '습도 센서', '2024-05-17 00:57:40.241441', 5, 'HCM', 'Test', '1', 'Y', '2024-05-17 00:57:40.245669', '2024-05-17 00:57:40.245701', 6, 1, 1, 1, NULL),
(7, '4cb46ee0-6a12-41cb-97fa-6263e712c21c', '컨테이너명', '2024-05-17 04:30:25.933785', 12, 'HCM', 'Test', '1', 'N', '2024-05-17 04:30:25.939840', '2024-05-17 04:30:25.939867', 7, 1, 19, 1, NULL),
(8, 'b9264608-95bd-40fd-99eb-0478c4e215dd', '컨트롤러', '2024-05-17 04:30:38.660987', 1, 'HCM', 'Test', '1', 'N', '2024-05-17 04:30:38.667208', '2024-05-17 04:30:38.667243', 8, 1, 19, 1, NULL),
(9, '0ea26a7f-188c-44f8-980e-f42f0228a916', '컨테이너명', '2024-05-17 04:51:58.457486', 10, 'HCM', 'Test', '1', 'N', '2024-05-17 04:51:58.463068', '2024-05-17 04:51:58.463098', 9, 1, 19, 1, NULL),
(10, '2b8650b9-1498-4c42-830f-94682e7a00d4', '컨트롤러', '2024-05-17 04:52:10.606134', 1, 'HCM', 'Test', '1', 'N', '2024-05-17 04:52:10.608349', '2024-05-17 04:52:10.608365', 10, 1, 19, 1, NULL),
(11, '28563215-2d92-4d15-a147-441d9a624e80', 'duvbba', '2024-05-17 04:52:27.621070', 1, 'HCM', 'Test', '1', 'N', '2024-05-17 04:52:27.623147', '2024-05-17 04:52:27.623161', 11, 1, 19, 1, NULL),
(12, '6326ca8d-36a0-433e-b7f5-57ec0cd1d6ad', '그린', '2024-05-17 04:52:46.233288', 1, 'HCM', 'Test', '1', 'Y', '2024-05-17 04:52:46.237182', '2024-05-17 04:52:46.237212', 12, 1, 19, 1, NULL);



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;