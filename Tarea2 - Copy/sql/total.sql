-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema tarea2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema tarea2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tarea2` DEFAULT CHARACTER SET utf8 ;
USE `tarea2` ;

-- -----------------------------------------------------
-- Table `tarea2`.`region`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`region` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tarea2`.`comuna`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`comuna` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  `region_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_comuna_region1`
    FOREIGN KEY (`region_id`)
    REFERENCES `tarea2`.`region` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_comuna_region1_idx` ON `tarea2`.`comuna` (`region_id` ASC);


-- -----------------------------------------------------
-- Table `tarea2`.`avistamiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`avistamiento` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comuna_id` INT NOT NULL,
  `dia_hora` DATETIME NOT NULL,
  `sector` VARCHAR(200) NULL,
  `nombre` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `celular` VARCHAR(15) NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_domicilio_comuna1`
    FOREIGN KEY (`comuna_id`)
    REFERENCES `tarea2`.`comuna` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_domicilio_comuna1_idx` ON `tarea2`.`avistamiento` (`comuna_id` ASC);


-- -----------------------------------------------------
-- Table `tarea2`.`detalle_avistamiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`detalle_avistamiento` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `dia_hora` DATETIME NOT NULL,
  `tipo` ENUM('no s??', 'insecto', 'ar??cnido', 'miri??podo') NOT NULL,
  `estado` ENUM('no s??', 'vivo', 'muerto') NOT NULL,
  `avistamiento_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_detalle_avistamiento_avistamiento1`
    FOREIGN KEY (`avistamiento_id`)
    REFERENCES `tarea2`.`avistamiento` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_detalle_avistamiento_avistamiento1_idx` ON `tarea2`.`detalle_avistamiento` (`avistamiento_id` ASC);


-- -----------------------------------------------------
-- Table `tarea2`.`foto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tarea2`.`foto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ruta_archivo` VARCHAR(300) NOT NULL,
  `nombre_archivo` VARCHAR(300) NOT NULL,
  `detalle_avistamiento_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_foto_detalle_avistamiento1`
    FOREIGN KEY (`detalle_avistamiento_id`)
    REFERENCES `tarea2`.`detalle_avistamiento` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_foto_detalle_avistamiento1_idx` ON `tarea2`.`foto` (`detalle_avistamiento_id` ASC);

INSERT INTO region (id, nombre) VALUES (1,'Regi??n de Tarapac??');
INSERT INTO region (id, nombre) VALUES (2,'Regi??n de Antofagasta');
INSERT INTO region (id, nombre) VALUES (3,'Regi??n de Atacama');
INSERT INTO region (id, nombre) VALUES (4,'Regi??n de Coquimbo ');
INSERT INTO region (id, nombre) VALUES (5,'Regi??n de Valpara??so');
INSERT INTO region (id, nombre) VALUES (6,'Regi??n del Libertador Bernardo Ohiggins');
INSERT INTO region (id, nombre) VALUES (7,'Regi??n del Maule');
INSERT INTO region (id, nombre) VALUES (8,'Regi??n del Biob??o');
INSERT INTO region (id, nombre) VALUES (9,'Regi??n de La Araucan??a');
INSERT INTO region (id, nombre) VALUES (10,'Regi??n de Los Lagos');
INSERT INTO region (id, nombre) VALUES (11,'Regi??n Ais??n del General Carlos Ib????ez del Campo');
INSERT INTO region (id, nombre) VALUES (12,'Regi??n de Magallanes y la Ant??rtica Chilena');
INSERT INTO region (id, nombre) VALUES (13,'Regi??n Metropolitana de Santiago ');
INSERT INTO region (id, nombre) VALUES (14,'Regi??n de Los R??os');
INSERT INTO region (id, nombre) VALUES (15,'Regi??n Arica y Parinacota');
INSERT INTO region (id, nombre) VALUES (16,'Regi??n del ??uble');


INSERT INTO comuna (region_id, id, nombre) VALUES (1, 10301, 'Cami??a');
INSERT INTO comuna (region_id, id, nombre) VALUES (1, 10302, 'Huara');
INSERT INTO comuna (region_id, id, nombre) VALUES (1, 10303, 'Pozo Almonte');
INSERT INTO comuna (region_id, id, nombre) VALUES (1, 10304, 'Iquique');
INSERT INTO comuna (region_id, id, nombre) VALUES (1, 10305, 'Pica');
INSERT INTO comuna (region_id, id, nombre) VALUES (1, 10306, 'Colchane');
INSERT INTO comuna (region_id, id, nombre) VALUES (1, 10307, 'Alto Hospicio');
INSERT INTO comuna (region_id, id, nombre) VALUES (2, 20101, 'Tocopilla');
INSERT INTO comuna (region_id, id, nombre) VALUES (2, 20102, 'Maria Elena');
INSERT INTO comuna (region_id, id, nombre) VALUES (2, 20201, 'Ollague');
INSERT INTO comuna (region_id, id, nombre) VALUES (2, 20202, 'Calama');
INSERT INTO comuna (region_id, id, nombre) VALUES (2, 20203, 'San Pedro Atacama');
INSERT INTO comuna (region_id, id, nombre) VALUES (2, 20301, 'Sierra Gorda');
INSERT INTO comuna (region_id, id, nombre) VALUES (2, 20302, 'Mejillones');
INSERT INTO comuna (region_id, id, nombre) VALUES (2, 20303, 'Antofagasta');
INSERT INTO comuna (region_id, id, nombre) VALUES (2, 20304, 'Taltal');
INSERT INTO comuna (region_id, id, nombre) VALUES (3, 30101, 'Diego de Almagro');
INSERT INTO comuna (region_id, id, nombre) VALUES (3, 30102, 'Cha??aral');
INSERT INTO comuna (region_id, id, nombre) VALUES (3, 30201, 'Caldera');
INSERT INTO comuna (region_id, id, nombre) VALUES (3, 30202, 'Copiapo');
INSERT INTO comuna (region_id, id, nombre) VALUES (3, 30203, 'Tierra Amarilla');
INSERT INTO comuna (region_id, id, nombre) VALUES (3, 30301, 'Huasco');
INSERT INTO comuna (region_id, id, nombre) VALUES (3, 30302, 'Freirina');
INSERT INTO comuna (region_id, id, nombre) VALUES (3, 30303, 'Vallenar');
INSERT INTO comuna (region_id, id, nombre) VALUES (3, 30304, 'Alto del Carmen');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40101, 'La Higuera');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40102, 'La Serena');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40103, 'Vicu??a');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40104, 'Paihuano');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40105, 'Coquimbo');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40106, 'Andacollo');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40201, 'Rio Hurtado');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40202, 'Ovalle');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40203, 'Monte Patria');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40204, 'Punitaqui');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40205, 'Combarbala');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40301, 'Mincha');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40302, 'Illapel');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40303, 'Salamanca');
INSERT INTO comuna (region_id, id, nombre) VALUES (4, 40304, 'Los Vilos');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50101, 'Petorca');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50102, 'Cabildo');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50103, 'Papudo');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50104, 'La Ligua');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50105, 'Zapallar');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50201, 'Putaendo');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50202, 'Santa Maria');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50203, 'San Felipe');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50204, 'Pencahue');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50205, 'Catemu');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50206, 'Llay Llay');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50301, 'Nogales');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50302, 'La Calera');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50303, 'Hijuelas');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50304, 'La Cruz');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50305, 'Quillota');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50306, 'Olmue');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50307, 'Limache');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50401, 'Los Andes');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50402, 'Rinconada');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50403, 'Calle Larga');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50404, 'San Esteban');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50501, 'Puchuncavi');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50502, 'Quintero');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50503, 'Vi??a del Mar');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50504, 'Villa Alemana');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50505, 'Quilpue');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50506, 'Valparaiso');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50507, 'Juan Fernandez');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50508, 'Casablanca');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50509, 'Concon');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50601, 'Isla de Pascua');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50701, 'Algarrobo');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50702, 'El Quisco');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50703, 'El Tabo');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50704, 'Cartagena');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50705, 'San Antonio');
INSERT INTO comuna (region_id, id, nombre) VALUES (5, 50706, 'Santo Domingo');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60101, 'Mostazal');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60102, 'Codegua');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60103, 'Graneros');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60104, 'Machali');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60105, 'Rancagua');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60106, 'Olivar');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60107, 'Do??ihue');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60108, 'Requinoa');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60109, 'Coinco');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60110, 'Coltauco');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60111, 'Quinta Tilcoco');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60112, 'Las Cabras');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60113, 'Rengo');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60114, 'Peumo');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60115, 'Pichidegua');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60116, 'Malloa');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60117, 'San Vicente');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60201, 'Navidad');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60202, 'La Estrella');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60203, 'Marchigue');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60204, 'Pichilemu');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60205, 'Litueche');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60206, 'Paredones');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60301, 'San Fernando');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60302, 'Peralillo');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60303, 'Placilla');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60304, 'Chimbarongo');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60305, 'Palmilla');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60306, 'Nancagua');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60307, 'Santa Cruz');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60308, 'Pumanque');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60309, 'Chepica');
INSERT INTO comuna (region_id, id, nombre) VALUES (6, 60310, 'Lolol');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70101, 'Teno');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70102, 'Romeral');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70103, 'Rauco');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70104, 'Curico');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70105, 'Sagrada Familia');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70106, 'Huala??e');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70107, 'Vichuquen');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70108, 'Molina');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70109, 'Licanten');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70201, 'Rio Claro');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70202, 'Curepto');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70203, 'Pelarco');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70204, 'Talca');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70205, 'Pencahue');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70206, 'San Clemente');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70207, 'Constitucion');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70208, 'Maule');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70209, 'Empedrado');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70210, 'San Rafael');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70301, 'San Javier');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70302, 'Colbun');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70303, 'Villa Alegre');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70304, 'Yerbas Buenas');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70305, 'Linares');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70306, 'Longavi');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70307, 'Retiro');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70308, 'Parral');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70401, 'Chanco');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70402, 'Pelluhue');
INSERT INTO comuna (region_id, id, nombre) VALUES (7, 70403, 'Cauquenes');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80101, 'Cobquecura');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80102, '??iquen');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80103, 'San Fabian');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80104, 'San Carlos');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80105, 'Quirihue');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80106, 'Ninhue');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80107, 'Trehuaco');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80108, 'San Nicolas');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80109, 'Coihueco');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80110, 'Chillan');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80111, 'Portezuelo');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80112, 'Pinto');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80113, 'Coelemu');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80114, 'Bulnes');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80115, 'San Ignacio');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80116, 'Ranquil');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80117, 'Quillon');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80118, 'El Carmen');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80119, 'Pemuco');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80120, 'Yungay');
INSERT INTO comuna (region_id, id, nombre) VALUES (16, 80121, 'Chillan Viejo');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80201, 'Tome');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80202, 'Florida');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80203, 'Penco');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80204, 'Talcahuano');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80205, 'Concepcion');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80206, 'Hualqui');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80207, 'Coronel');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80208, 'Lota');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80209, 'Santa Juana');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80210, 'Chiguayante');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80211, 'San Pedro de la Paz');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80212, 'Hualpen');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80301, 'Cabrero');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80302, 'Yumbel');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80303, 'Tucapel');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80304, 'Antuco');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80305, 'San Rosendo');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80306, 'Laja');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80307, 'Quilleco');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80308, 'Los Angeles');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80309, 'Nacimiento');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80310, 'Negrete');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80311, 'Santa Barbara');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80312, 'Quilaco');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80313, 'Mulchen');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80314, 'Alto Bio Bio');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80401, 'Arauco');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80402, 'Curanilahue');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80403, 'Los Alamos');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80404, 'Lebu');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80405, 'Ca??ete');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80406, 'Contulmo');
INSERT INTO comuna (region_id, id, nombre) VALUES (8, 80407, 'Tirua');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90101, 'Renaico');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90102, 'Angol');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90103, 'Collipulli');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90104, 'Los Sauces');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90105, 'Puren');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90106, 'Ercilla');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90107, 'Lumaco');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90108, 'Victoria');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90109, 'Traiguen');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90110, 'Curacautin');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90111, 'Lonquimay');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90201, 'Perquenco');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90202, 'Galvarino');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90203, 'Lautaro');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90204, 'Vilcun');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90205, 'Temuco');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90206, 'Carahue');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90207, 'Melipeuco');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90208, 'Nueva Imperial');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90209, 'Puerto Saavedra');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90210, 'Cunco');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90211, 'Freire');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90212, 'Pitrufquen');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90213, 'Teodoro Schmidt');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90214, 'Gorbea');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90215, 'Pucon');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90216, 'Villarrica');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90217, 'Tolten');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90218, 'Curarrehue');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90219, 'Loncoche');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90220, 'Padre Las Casas');
INSERT INTO comuna (region_id, id, nombre) VALUES (9, 90221, 'Cholchol');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100201, 'San Pablo');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100202, 'San Juan');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100203, 'Osorno');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100204, 'Puyehue');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100205, 'Rio Negro');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100206, 'Purranque');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100207, 'Puerto Octay');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100301, 'Frutillar');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100302, 'Fresia');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100303, 'Llanquihue');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100304, 'Puerto Varas');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100305, 'Los Muermos');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100306, 'Puerto Montt');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100307, 'Maullin');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100308, 'Calbuco');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100309, 'Cochamo');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100401, 'Ancud');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100402, 'Quemchi');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100403, 'Dalcahue');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100404, 'Curaco de Velez');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100405, 'Castro');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100406, 'Chonchi');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100407, 'Queilen');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100408, 'Quellon');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100409, 'Quinchao');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100410, 'Puqueldon');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100501, 'Chaiten');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100502, 'Futaleufu');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100503, 'Palena');
INSERT INTO comuna (region_id, id, nombre) VALUES (10, 100504, 'Hualaihue');
INSERT INTO comuna (region_id, id, nombre) VALUES (11, 110101, 'Guaitecas');
INSERT INTO comuna (region_id, id, nombre) VALUES (11, 110102, 'Cisnes');
INSERT INTO comuna (region_id, id, nombre) VALUES (11, 110103, 'Aysen');
INSERT INTO comuna (region_id, id, nombre) VALUES (11, 110201, 'Coyhaique');
INSERT INTO comuna (region_id, id, nombre) VALUES (11, 110202, 'Lago Verde');
INSERT INTO comuna (region_id, id, nombre) VALUES (11, 110301, 'Rio Iba?ez');
INSERT INTO comuna (region_id, id, nombre) VALUES (11, 110302, 'Chile Chico');
INSERT INTO comuna (region_id, id, nombre) VALUES (11, 110401, 'Cochrane');
INSERT INTO comuna (region_id, id, nombre) VALUES (11, 110402, 'Tortel');
INSERT INTO comuna (region_id, id, nombre) VALUES (11, 110403, 'O''Higins');
INSERT INTO comuna (region_id, id, nombre) VALUES (12, 120101, 'Torres del Paine');
INSERT INTO comuna (region_id, id, nombre) VALUES (12, 120102, 'Puerto Natales');
INSERT INTO comuna (region_id, id, nombre) VALUES (12, 120201, 'Laguna Blanca');
INSERT INTO comuna (region_id, id, nombre) VALUES (12, 120202, 'San Gregorio');
INSERT INTO comuna (region_id, id, nombre) VALUES (12, 120203, 'Rio Verde');
INSERT INTO comuna (region_id, id, nombre) VALUES (12, 120204, 'Punta Arenas');
INSERT INTO comuna (region_id, id, nombre) VALUES (12, 120301, 'Porvenir');
INSERT INTO comuna (region_id, id, nombre) VALUES (12, 120302, 'Primavera');
INSERT INTO comuna (region_id, id, nombre) VALUES (12, 120303, 'Timaukel');
INSERT INTO comuna (region_id, id, nombre) VALUES (12, 120401, 'Antartica');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130101, 'Tiltil');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130102, 'Colina');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130103, 'Lampa');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130201, 'Conchali');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130202, 'Quilicura');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130203, 'Renca');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130204, 'Las Condes');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130205, 'Pudahuel');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130206, 'Quinta Normal');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130207, 'Providencia');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130208, 'Santiago');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130209, 'La Reina');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130210, '??u??oa');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130211, 'San Miguel');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130212, 'Maipu');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130213, 'La Cisterna');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130214, 'La Florida');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130215, 'La Granja');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130216, 'Independencia');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130217, 'Huechuraba');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130218, 'Recoleta');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130219, 'Vitacura');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130220, 'Lo Barrenechea');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130221, 'Macul');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130222, 'Pe??alolen');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130223, 'San Joaquin');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130224, 'La Pintana');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130225, 'San Ramon');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130226, 'El Bosque');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130227, 'Pedro Aguirre Cerda');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130228, 'Lo Espejo');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130229, 'Estacion Central');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130230, 'Cerrillos');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130231, 'Lo Prado');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130232, 'Cerro Navia');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130301, 'San Jose de Maipo');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130302, 'Puente Alto');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130303, 'Pirque');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130401, 'San Bernardo');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130402, 'Calera de Tango');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130403, 'Buin');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130404, 'Paine');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130501, 'Pe??aflor');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130502, 'Talagante');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130503, 'El Monte');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130504, 'Isla de Maipo');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130601, 'Curacavi');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130602, 'Maria Pinto');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130603, 'Melipilla');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130604, 'San Pedro');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130605, 'Alhue');
INSERT INTO comuna (region_id, id, nombre) VALUES (13, 130606, 'Padre Hurtado');
INSERT INTO comuna (region_id, id, nombre) VALUES (14, 100101, 'Lanco');
INSERT INTO comuna (region_id, id, nombre) VALUES (14, 100102, 'Mariquina');
INSERT INTO comuna (region_id, id, nombre) VALUES (14, 100103, 'Panguipulli');
INSERT INTO comuna (region_id, id, nombre) VALUES (14, 100104, 'Mafil');
INSERT INTO comuna (region_id, id, nombre) VALUES (14, 100105, 'Valdivia');
INSERT INTO comuna (region_id, id, nombre) VALUES (14, 100106, 'Los Lagos');
INSERT INTO comuna (region_id, id, nombre) VALUES (14, 100107, 'Corral');
INSERT INTO comuna (region_id, id, nombre) VALUES (14, 100108, 'Paillaco');
INSERT INTO comuna (region_id, id, nombre) VALUES (14, 100109, 'Futrono');
INSERT INTO comuna (region_id, id, nombre) VALUES (14, 100110, 'Lago Ranco');
INSERT INTO comuna (region_id, id, nombre) VALUES (14, 100111, 'La Union');
INSERT INTO comuna (region_id, id, nombre) VALUES (14, 100112, 'Rio Bueno');
INSERT INTO comuna (region_id, id, nombre) VALUES (15, 10101, 'Gral. Lagos');
INSERT INTO comuna (region_id, id, nombre) VALUES (15, 10102, 'Putre');
INSERT INTO comuna (region_id, id, nombre) VALUES (15, 10201, 'Arica');
INSERT INTO comuna (region_id, id, nombre) VALUES (15, 10202, 'Camarones');


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
