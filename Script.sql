CREATE USER 'user_ptyhon'@'localhost' IDENTIFIED BY 'Clas3s1Nt2024_!';
GRANT CREATE, INSERT, UPDATE, DELETE, SELECT, FILE, EXECUTE ON *.* TO 'user_ptyhon'@'localhost' WITH GRANT OPTION;

CREATE DATABASE db_universidad;

CREATE TABLE `db_universidad`.`estados` (
	`id` INT AUTO_INCREMENT NOT NULL,
    `nombre` VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY(`id`)
);

CREATE TABLE `db_universidad`.`personas` (
	`id` INT AUTO_INCREMENT NOT NULL,
    `cedula` VARCHAR(50) NOT NULL UNIQUE,
    `nombre` VARCHAR(250) NOT NULL,
	`estado` INT NOT NULL,
	`fecha` DATETIME NOT NULL,
	`activo` BIT NOT NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_personas__estados` FOREIGN KEY (`estado`) REFERENCES `estados`(`id`)
);

INSERT INTO `db_universidad`.`estados` (`nombre`) VALUES ('Solter@s');
INSERT INTO `db_universidad`.`personas` (`cedula`, `nombre`, `estado`, `fecha`, `activo`) 
VALUES ('6546465', 'Pepito Perez', 1, NOW(), 1);