CREATE TABLE IF NOT EXISTS `Beer-Profile` ( 
`ID` int(1) NOT NULL auto_increment, 
`Name` varchar(40) NOT NULL, 
PRIMARY KEY (`ID`) 
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ; 

INSERT INTO `Beer-Profile` (`Name`) VALUES 
('Brand Name 1'), 
('Brand Name 2'), 
('Brand Name 3'), 
('Brand Name 4');

CREATE TABLE IF NOT EXISTS `Bitterness` ( 
`ID` int(1) NOT NULL auto_increment,
`IBU` varchar(40) NOT NULL,
PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1; 

INSERT INTO `Bitterness` (`IBU`) VALUES 
('64.0'), 
('29.8'), 
('49.6'), 
('57.3'),
('20');

CREATE TABLE IF NOT EXISTS `AlcoholbyVolume` ( 
`ID` int(1) NOT NULL auto_increment,
`ABV` varchar(40) NOT NULL,
PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1; 

INSERT INTO `AlcoholbyVolume` (`ABV`) VALUES 
('8.3'), 
('8.2'), 
('6.2'), 
('7.2'),
('5.8');
