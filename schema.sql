-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- Schema mulheres_na_ti
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mulheres_na_ti` DEFAULT CHARACTER SET utf8 ;
USE `mulheres_na_ti`

-- Create Table cotistas
CREATE TABLE IF NOT EXISTS `mulheres_na_ti`.`cotistas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `discente` VARCHAR(50),
  `sexo` VARCHAR(1) NULL,
  `nota_final` DOUBLE NULL,
  `cotista` VARCHAR(1) NULL,
  `cep`VARCHAR(10) NULL,
  `descricao`VARCHAR(20) NULL,

   PRIMARY KEY (`id`))
ENGINE = InnoDB;