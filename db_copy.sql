-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Wersja serwera:               10.5.10-MariaDB - mariadb.org binary distribution
-- Serwer OS:                    Win64
-- HeidiSQL Wersja:              11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Zrzucanie danych dla tabeli ioproject.auth_group: ~0 rows (około)
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

-- Zrzucanie danych dla tabeli ioproject.auth_group_permissions: ~0 rows (około)
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

-- Zrzucanie danych dla tabeli ioproject.auth_permission: ~24 rows (około)
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
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
	(24, 'Can view session', 6, 'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

-- Zrzucanie danych dla tabeli ioproject.auth_user: ~2 rows (około)
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$260000$kWpBnx3IwMorjncaKJ8DL9$UiKaOh91aNIHeZbcq/e4RZ0bzjhB05VmByQBdMvX72c=', '2021-06-09 09:06:23.010892', 1, 'admin', '', '', '', 1, 1, '2021-06-05 08:37:26.595295'),
	(2, 'pbkdf2_sha256$260000$0gZ1w9lzH436Y3MxdkUzgv$OGjvjbFiYiHYeX5zfZW2FQrhcUBEf9XWEayfyDYk6lE=', '2021-06-09 09:06:41.641623', 0, 'student1', '', '', '', 0, 1, '2021-06-08 09:57:26.750471');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

-- Zrzucanie danych dla tabeli ioproject.auth_user_groups: ~0 rows (około)
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

-- Zrzucanie danych dla tabeli ioproject.auth_user_user_permissions: ~0 rows (około)
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

-- Zrzucanie danych dla tabeli ioproject.django_admin_log: ~3 rows (około)
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2021-06-05 08:39:53.222854', '1', 'Nauczyciele', 1, '[{"added": {}}]', 3, 1),
	(2, '2021-06-05 08:40:49.052292', '1', 'Nauczyciele', 3, '', 3, 1),
	(3, '2021-06-08 09:57:26.964923', '2', 'student1', 1, '[{"added": {}}]', 4, 1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

-- Zrzucanie danych dla tabeli ioproject.django_content_type: ~6 rows (około)
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(6, 'sessions', 'session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

-- Zrzucanie danych dla tabeli ioproject.django_migrations: ~18 rows (około)
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2021-06-05 08:36:54.290661'),
	(2, 'auth', '0001_initial', '2021-06-05 08:36:55.010820'),
	(3, 'admin', '0001_initial', '2021-06-05 08:36:55.155704'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2021-06-05 08:36:55.178868'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-06-05 08:36:55.195859'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2021-06-05 08:36:55.279810'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2021-06-05 08:36:55.345772'),
	(8, 'auth', '0003_alter_user_email_max_length', '2021-06-05 08:36:55.411424'),
	(9, 'auth', '0004_alter_user_username_opts', '2021-06-05 08:36:55.424416'),
	(10, 'auth', '0005_alter_user_last_login_null', '2021-06-05 08:36:55.480385'),
	(11, 'auth', '0006_require_contenttypes_0002', '2021-06-05 08:36:55.485381'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2021-06-05 08:36:55.498376'),
	(13, 'auth', '0008_alter_user_username_max_length', '2021-06-05 08:36:55.531358'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2021-06-05 08:36:55.563337'),
	(15, 'auth', '0010_alter_group_name_max_length', '2021-06-05 08:36:55.636295'),
	(16, 'auth', '0011_update_proxy_permissions', '2021-06-05 08:36:55.652287'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2021-06-05 08:36:55.687267'),
	(18, 'sessions', '0001_initial', '2021-06-05 08:36:55.768220');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

-- Zrzucanie danych dla tabeli ioproject.django_session: ~1 rows (około)
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('6k5laoju1x97o8qu6370bb9reui3m9b6', '.eJxVjEEOwiAUBe_C2hA-FAGX7j1D84CPrRqalHZlvLsh6UK3M5N5ixH7No1743Wcs7gILU6_LCI9uXaRH6j3RaalbuscZU_kYZu8LZlf16P9G0xoU9_6yMGZqL2CjkSDs2zhyVitCYpSIs4qDDQACraYeAYb41BKQC5BfL7JNTfg:1lquAb:JLGUFnEmVfmvHFHSIT7JE0RFSZzBRwLTfleMbCN-L10', '2021-06-23 09:06:41.643622');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
