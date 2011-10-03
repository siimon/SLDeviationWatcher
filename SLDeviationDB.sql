SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

CREATE TABLE IF NOT EXISTS `Deviation` (
    `DeviationID` int(11) NOT NULL AUTO_INCREMENT,
    `Reason` text COLLATE utf8_swedish_ci NOT NULL,
    `DeviationTime` datetime NOT NULL,
    PRIMARY KEY (`DeviationID`)
    ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci AUTO_INCREMENT=7 ;

