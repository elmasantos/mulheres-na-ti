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
  `cep`VARCHAR(10) NULL,
  `cotista` VARCHAR(1) NULL,
  `forma_ingresso` VARCHAR(100) NULL,
  `nivel_ensino`VARCHAR(100) NULL,

   PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mulheres_na_ti`.`matricula2016_1` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_turma` VARCHAR(50),
  `discente` VARCHAR(50),
  `id_curso` VARCHAR(50),
  `unidade` VARCHAR(10) NULL,
  `nota` VARCHAR(10) NULL,
  `reposicao` VARCHAR(1) NULL,
  `media_final` VARCHAR(100) NULL,
  `numero_total_faltas` VARCHAR(100) NULL,
  `descricao` VARCHAR(50),

   PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mulheres_na_ti`.`matricula2016_2` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_turma` VARCHAR(50),
  `discente` VARCHAR(50),
  `id_curso` VARCHAR(50),
  `unidade` VARCHAR(10) NULL,
  `nota` VARCHAR(10) NULL,
  `reposicao` VARCHAR(1) NULL,
  `media_final` VARCHAR(100) NULL,
  `numero_total_faltas` VARCHAR(100) NULL,
  `descricao` VARCHAR(50),

   PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mulheres_na_ti`.`matricula2015_1` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_turma` VARCHAR(50),
  `discente` VARCHAR(50),
  `id_curso` VARCHAR(50),
  `unidade` VARCHAR(10) NULL,
  `nota` VARCHAR(10) NULL,
  `reposicao` VARCHAR(1) NULL,
  `media_final` VARCHAR(100) NULL,
  `numero_total_faltas` VARCHAR(100) NULL,
  `descricao` VARCHAR(50),

   PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mulheres_na_ti`.`matricula2015_2` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_turma` VARCHAR(50),
  `discente` VARCHAR(50),
  `id_curso` VARCHAR(50),
  `unidade` VARCHAR(10) NULL,
  `nota` VARCHAR(10) NULL,
  `reposicao` VARCHAR(1) NULL,
  `media_final` VARCHAR(100) NULL,
  `numero_total_faltas` VARCHAR(100) NULL,
  `descricao` VARCHAR(50),

   PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mulheres_na_ti`.`matricula2014_1` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_turma` VARCHAR(50),
  `discente` VARCHAR(50),
  `id_curso` VARCHAR(50),
  `unidade` VARCHAR(10) NULL,
  `nota` VARCHAR(10) NULL,
  `reposicao` VARCHAR(1) NULL,
  `media_final` VARCHAR(100) NULL,
  `numero_total_faltas` VARCHAR(100) NULL,
  `descricao` VARCHAR(50),

   PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mulheres_na_ti`.`matricula2014_2` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `id_turma` VARCHAR(50),
  `discente` VARCHAR(50),
  `id_curso` VARCHAR(50),
  `unidade` VARCHAR(10) NULL,
  `nota` VARCHAR(10) NULL,
  `reposicao` VARCHAR(1) NULL,
  `media_final` VARCHAR(100) NULL,
  `numero_total_faltas` VARCHAR(100) NULL,
  `descricao` VARCHAR(50),

   PRIMARY KEY (`id`))
ENGINE = InnoDB;
