-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 07, 2017 at 06:32 AM
-- Server version: 5.5.53-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `group_assignment_tool`
--

-- --------------------------------------------------------

--
-- Table structure for table `app`
--

CREATE TABLE IF NOT EXISTS `app` (
  `app_id` smallint(6) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  `token` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`app_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `app`
--

INSERT INTO `app` (`app_id`, `name`, `token`) VALUES
(1, 'Slack', ''),
(2, 'Bugzilla', ''),
(3, 'Smartsheet', ''),
(10, 'Eleven', '');

-- --------------------------------------------------------

--
-- Table structure for table `app_group`
--

CREATE TABLE IF NOT EXISTS `app_group` (
  `app_id` smallint(6) NOT NULL,
  `group_id` smallint(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `app_group`
--

INSERT INTO `app_group` (`app_id`, `group_id`) VALUES
(1, 32767),
(2, 32767);

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE IF NOT EXISTS `employee` (
  `empl_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL DEFAULT '',
  `last_name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`email`),
  UNIQUE KEY `empl_id` (`empl_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`empl_id`, `email`, `first_name`, `last_name`) VALUES
(1, 'elgandara@csumb.edu', 'Eliasar', 'Gandara'),
(2, 'fakeemail@fake.edu', 'fake', 'person');

-- --------------------------------------------------------

--
-- Table structure for table `employee_role`
--

CREATE TABLE IF NOT EXISTS `employee_role` (
  `email` varchar(255) NOT NULL COMMENT 'The email belonging to an employee',
  `role_id` smallint(6) NOT NULL COMMENT 'The id of a role.',
  PRIMARY KEY (`email`,`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee_role`
--

INSERT INTO `employee_role` (`email`, `role_id`) VALUES
('elgandara@csumb.edu', 11111),
('fakeemail@fake.edu', 22222);

-- --------------------------------------------------------

--
-- Table structure for table `group`
--

CREATE TABLE IF NOT EXISTS `group` (
  `group_id` smallint(6) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`group_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=32769 ;

--
-- Dumping data for table `group`
--

INSERT INTO `group` (`group_id`, `name`) VALUES
(32767, 'someGroupA'),
(32768, 'groupingB');

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE IF NOT EXISTS `role` (
  `role_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(1000) NOT NULL,
  PRIMARY KEY (`role_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=22223 ;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`role_id`, `name`, `description`) VALUES
(11111, 'kunf_fu_master', 'kung fu fighting'),
(22222, 'gym_teacher', 'teach gym');

-- --------------------------------------------------------

--
-- Table structure for table `role_group`
--

CREATE TABLE IF NOT EXISTS `role_group` (
  `role_id` smallint(6) unsigned NOT NULL,
  `group_id` smallint(6) NOT NULL,
  PRIMARY KEY (`role_id`,`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `role_group`
--

INSERT INTO `role_group` (`role_id`, `group_id`) VALUES
(11111, 32767),
(22222, 32767);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `email` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `is_admin` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`email`, `first_name`, `last_name`, `username`, `password`, `is_admin`) VALUES
('elgandara@csumb.edu', 'Eliasar', 'Gandara', 'eliasar', '*58C036CDA51D8E8BBBBF2F9EA5ABF111ADA444F0', 1);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
