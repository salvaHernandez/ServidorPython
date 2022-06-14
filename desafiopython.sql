-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-06-2022 a las 13:18:13
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `desafiopython`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `controlencuesta`
--

CREATE TABLE `controlencuesta` (
  `nombreEncuesta` varchar(20) DEFAULT NULL,
  `activada` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `controlencuesta`
--

INSERT INTO `controlencuesta` (`nombreEncuesta`, `activada`) VALUES
('Cine', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `encuesta`
--

CREATE TABLE `encuesta` (
  `idEncuesta` int(11) NOT NULL,
  `seriePeli` text DEFAULT NULL,
  `saga` text DEFAULT NULL,
  `generoPreferido` text DEFAULT NULL,
  `numPelis` int(11) DEFAULT NULL,
  `anime` int(11) DEFAULT NULL,
  `valoracion` int(11) DEFAULT NULL,
  `nombreUsu` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `encuesta`
--

INSERT INTO `encuesta` (`idEncuesta`, `seriePeli`, `saga`, `generoPreferido`, `numPelis`, `anime`, `valoracion`, `nombreUsu`) VALUES
(24, 'Peliculas', 'Sir de los anillos', 'Accion,Ciencia Ficcion', 6, 0, 5, 'Mario'),
(25, 'Peliculas', 'Sir de los anillos', 'Ciencia Ficcion,Romanticas', 7, 1, 6, 'Mario'),
(26, 'Peliculas', 'Sir de los anillos', 'Accion', 0, 0, 0, 'Mario'),
(27, 'Peliculas', 'Sir de los anillos', 'Accion,Ciencia Ficcion', 0, 0, 0, 'Mario'),
(28, 'Peliculas', 'Sir de los anillos', 'Accion,Ciencia Ficcion,Romanticas', 0, 0, 0, 'Mario'),
(29, 'Peliculas', 'Sir de los anillos', 'Ciencia Ficcion', 0, 0, 0, 'Mario'),
(30, 'Peliculas', 'Sir de los anillos', 'Romanticas', 0, 0, 0, 'Mario'),
(31, 'Peliculas', 'Sir de los anillos', 'Accion,Romanticas', 0, 0, 0, 'Mario'),
(32, 'Peliculas', 'Sir de los anillos', 'Ciencia Ficcion,Romanticas', 0, 0, 0, 'Mario'),
(33, 'Peliculas', 'Sir de los anillos', 'Accion,Ciencia Ficcion', 0, 0, 0, 'Mario'),
(34, 'Peliculas', 'Sir de los anillos', 'Accion', 0, 0, 0, 'Mario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `generos`
--

CREATE TABLE `generos` (
  `idGenero` int(11) NOT NULL,
  `genero` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `generos`
--

INSERT INTO `generos` (`idGenero`, `genero`) VALUES
(1, 'Accion'),
(2, 'Ciencia Ficcion'),
(3, 'Romanticas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `idRol` int(11) NOT NULL,
  `tipoRol` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`idRol`, `tipoRol`) VALUES
(1, 'Admin'),
(2, 'User');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `nombre` varchar(20) NOT NULL,
  `idRol` int(11) DEFAULT NULL,
  `pass` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`nombre`, `idRol`, `pass`) VALUES
('Mario', 2, '123456'),
('Salva', 1, '123456');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `encuesta`
--
ALTER TABLE `encuesta`
  ADD PRIMARY KEY (`idEncuesta`),
  ADD KEY `nombreUsu` (`nombreUsu`);

--
-- Indices de la tabla `generos`
--
ALTER TABLE `generos`
  ADD PRIMARY KEY (`idGenero`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`idRol`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`nombre`),
  ADD KEY `idRol` (`idRol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `encuesta`
--
ALTER TABLE `encuesta`
  MODIFY `idEncuesta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT de la tabla `generos`
--
ALTER TABLE `generos`
  MODIFY `idGenero` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `idRol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `encuesta`
--
ALTER TABLE `encuesta`
  ADD CONSTRAINT `encuesta_ibfk_1` FOREIGN KEY (`nombreUsu`) REFERENCES `usuario` (`nombre`) ON DELETE CASCADE;

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`idRol`) REFERENCES `roles` (`idRol`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
