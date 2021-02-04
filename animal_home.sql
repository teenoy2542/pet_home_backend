-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 16, 2020 at 03:38 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `animal_home`
--

-- --------------------------------------------------------

--
-- Table structure for table `interested`
--

CREATE TABLE `interested` (
  `Pet_ID` int(100) NOT NULL,
  `Username` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `interested`
--

INSERT INTO `interested` (`Pet_ID`, `Username`) VALUES
(1, 'inzee8633\r\n'),
(2, 'inzee8633\r\n'),
(3, 'gill_momo\r\n'),
(4, 'gill_momo\r\n'),
(5, 'pong_123\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `Message_ID` int(100) NOT NULL,
  `Pet_ID` int(100) NOT NULL,
  `Username` varchar(100) NOT NULL,
  `Message` varchar(300) NOT NULL,
  `Messsage_Date` date NOT NULL,
  `Message_Time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `message`
--

INSERT INTO `message` (`Message_ID`, `Pet_ID`, `Username`, `Message`, `Messsage_Date`, `Message_Time`) VALUES
(1, 1, 'sima_1160\r\n', 'สวัสดีครับ\r\n', '2020-02-16', '2020-12-16 14:29:50'),
(2, 1, 'sima_1160\r\n', 'พอดีอย่ากเลี้ยงแมวตัวนี้ต่อ\r\n', '2020-02-16', '2020-12-16 14:30:26'),
(3, 1, 'gill_momo\r\n', 'สวัสดีครับ น่ารักมากครับ อย่ากเลี้ยงต่อ\r\n', '2020-02-17', '2020-12-16 14:31:04'),
(4, 1, 'bee_win\r\n', 'สนใจแมวตัวนี้ครับ\r\n', '2020-02-18', '2020-12-16 14:31:32'),
(5, 3, 'pong_123\r\n', 'สนใจนกตัวนี้ครับ\r\n', '2020-02-18', '2020-12-16 14:31:58');

-- --------------------------------------------------------

--
-- Table structure for table `pet`
--

CREATE TABLE `pet` (
  `Pet_ID` int(100) NOT NULL,
  `Owner_Username` varchar(100) NOT NULL,
  `New_Owner_Username` varchar(100) DEFAULT NULL,
  `Type` varchar(10) NOT NULL,
  `Age` varchar(10) NOT NULL,
  `Sex` varchar(20) NOT NULL,
  `Disease` varchar(200) DEFAULT NULL,
  `Habit` varchar(250) DEFAULT NULL,
  `Status` varchar(50) NOT NULL,
  `Province` varchar(100) NOT NULL,
  `District` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pet`
--

INSERT INTO `pet` (`Pet_ID`, `Owner_Username`, `New_Owner_Username`, `Type`, `Age`, `Sex`, `Disease`, `Habit`, `Status`, `Province`, `District`) VALUES
(1, 'sima_1160\r\n', 'inwza11\r\n', 'แมว', '2 ปี', 'male', 'โรคหวัดแมว\r\n', 'ขี้เล่น\r\n', 'หาคนเลี้ยงต่อได้แล้ว', 'จังหวัดพะเยา\r\n', 'อำเภอเมือง \r\n'),
(2, 'inzee8633\r\n', 'cawwa55\r\n', 'แมว', '3 ปี', 'female', 'ไม่มี\r\n', 'ชอบเดินเล่น\r\n', 'หาคนเลี้ยงต่อได้แล้ว', 'จังหวัดชัยภูมิ\r\n', 'อำเภอชมพู \r\n'),
(3, 'gill_momo\r\n', NULL, 'นกแก้ว', '5 ปี', 'male', NULL, NULL, 'กำลังหาคนเลี้ยงต่อ', 'จังหวัดเชียงใหม่\r\n', 'อำเภอเมือง \r\n'),
(4, 'bee_win\r\n', 'opami_pa\r\n', 'สุนัข', '4 ปี', 'female', 'โรคผิวหนัง\r\n', NULL, 'หาคนเลี้ยงต่อได้แล้ว', 'จังหวัดเชียงราย\r\n', 'อำเภอเถิง \r\n'),
(5, 'pong_123\r\n', 'kwin_na\r\n', 'กระต่าย', '5 เดือน', 'male', NULL, 'ไม่ชอบให้จับ\r\n', 'หาคนเลี้ยงต่อได้แล้ว', 'จังหวัดพะเยา\r\n', 'อำเภอเมือง \r\n');

-- --------------------------------------------------------

--
-- Table structure for table `pet_photo`
--

CREATE TABLE `pet_photo` (
  `ID_Pet_Photo` int(100) NOT NULL,
  `Pet_ID` int(100) NOT NULL,
  `Photo` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pet_photo`
--

INSERT INTO `pet_photo` (`ID_Pet_Photo`, `Pet_ID`, `Photo`) VALUES
(1, 1, NULL),
(2, 1, NULL),
(3, 3, NULL),
(4, 4, NULL),
(5, 2, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `Username` varchar(100) NOT NULL,
  `Password` binary(20) NOT NULL,
  `FirstName` varchar(100) NOT NULL,
  `LastName` varchar(100) NOT NULL,
  `Phone` int(10) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Address` varchar(200) DEFAULT NULL,
  `Sex` varchar(10) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Photo` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`Username`, `Password`, `FirstName`, `LastName`, `Phone`, `Email`, `Address`, `Sex`, `Type`, `Photo`) VALUES
('bee_win\r\n', 0x0a1c6944cb66d02ccefac35620ce2e5100000000, 'ชนารดี\r\n', 'คงคะจันทร์ \r\n', 656226846, 'bee_win@gmail.com\r\n', 'อำเภอเถิง จังหวัดเชียงราย\r\n', 'male', 'หาสัตว์เลี้ยง', NULL),
('gill_momo\r\n', 0x3a50c0526bfb6f808dc697df5eb1f6ad00000000, 'ธนัชญา\r\n', 'คุปตัษเฐียร\r\n', 815616515, 'gill_momo@gmail.com\r\n', 'อำเภอเมือง จังหวัดเชียงใหม่\r\n', 'male', 'หาบ้านให้สัตว์เลี้ยง', NULL),
('inzee8633\r\n', 0xe908c02607fd0e339e8e3b5c0bdc8e9800000000, 'รติรัตน์\r\n', 'คุฑะสุต\r\n', 912468525, 'inzee8633@gmail.com\r\n', 'อำเภอชมพู จังหวัดชัยภูมิ\r\n', 'female', 'หาบ้านให้สัตว์เลี้ยง', NULL),
('pong_123\r\n', 0x31888b76fc870491b0b1d0c6642f9a9800000000, 'ชญานิศ\r\n', 'คชเสนี\r\n', 944531955, 'pong_123@gmail.com\r\n', 'อำเภอเมือง จังหวัดพะเยา\r\n', 'female', 'หาบ้านให้สัตว์เลี้ยง', NULL),
('sima_1160\r\n', 0x70862f51416c696fb0c0d9d73cc65f4200000000, 'ศุภมิตร\r\n', 'แปดทิพย์\r\n', 894156845, 'sima_1160@gmail.com\r\n', 'อำเภอเมือง จังหวัดพะเยา\r\n', 'male', 'หาสัตว์เลี้ยง', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `interested`
--
ALTER TABLE `interested`
  ADD KEY `Username` (`Username`),
  ADD KEY `Pet_ID` (`Pet_ID`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`Message_ID`),
  ADD KEY `User` (`Username`),
  ADD KEY `Pet` (`Pet_ID`);

--
-- Indexes for table `pet`
--
ALTER TABLE `pet`
  ADD PRIMARY KEY (`Pet_ID`),
  ADD KEY `FK` (`Owner_Username`) USING BTREE;

--
-- Indexes for table `pet_photo`
--
ALTER TABLE `pet_photo`
  ADD PRIMARY KEY (`ID_Pet_Photo`),
  ADD KEY `Pet_ID` (`Pet_ID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`Username`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `interested`
--
ALTER TABLE `interested`
  ADD CONSTRAINT `Pet_ID` FOREIGN KEY (`Pet_ID`) REFERENCES `pet` (`Pet_ID`),
  ADD CONSTRAINT `Username` FOREIGN KEY (`Username`) REFERENCES `user` (`Username`);

--
-- Constraints for table `message`
--
ALTER TABLE `message`
  ADD CONSTRAINT `Pet` FOREIGN KEY (`Pet_ID`) REFERENCES `pet` (`Pet_ID`),
  ADD CONSTRAINT `User` FOREIGN KEY (`Username`) REFERENCES `user` (`Username`);

--
-- Constraints for table `pet`
--
ALTER TABLE `pet`
  ADD CONSTRAINT `pet_ibfk_1` FOREIGN KEY (`Owner_Username`) REFERENCES `user` (`Username`);

--
-- Constraints for table `pet_photo`
--
ALTER TABLE `pet_photo`
  ADD CONSTRAINT `pet_photo_ibfk_1` FOREIGN KEY (`Pet_ID`) REFERENCES `pet` (`Pet_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
