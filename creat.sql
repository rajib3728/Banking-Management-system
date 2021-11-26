-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2021 at 07:03 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bankacc`
--

-- --------------------------------------------------------

--
-- Table structure for table `creat`
--

CREATE TABLE `creat` (
  `en` varchar(500) NOT NULL,
  `eoc` varchar(500) NOT NULL,
  `edp` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `creat`
--

INSERT INTO `creat` (`en`, `eoc`, `edp`) VALUES
('gfhgvjh', 'jhvjhb', 'yguyg'),
('uygyu', 'ugukj', 'ygyug'),
('uhiuh', 'jbkjh', 'uhiuh'),
('uhiuh', 'hjh', 'uhbjh'),
('uhiuh', 'hjh', 'uhbjh'),
('uhiuh', 'hjh', 'uhbjh'),
('uhiuh', 'hjh', 'uhbjh'),
('rajib', '500', '800'),
('Rajib', '888', '999'),
('Rajib', '888', '555'),
('suman', '500', '8888'),
('Raj', '1', '5'),
('eo', '55', '55'),
('ra', '55', '22'),
('565', '5165', '4654'),
('Raj', 'Raj@', '1234'),
('Raj', 'abc@', '1234'),
('abc', 'abc@', '12'),
('abc', 'abc@', '12'),
('ABC', 'ABC@', '123'),
('kk', 'ab@', 'kk'),
('4545', '51', '455'),
('plc', 'plc@', '123');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
