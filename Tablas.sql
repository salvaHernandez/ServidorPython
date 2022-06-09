create table roles(idRol integer primary key AUTO_INCREMENT, tipoRol text)

create table generos(idGenero int primary key AUTO_INCREMENT, genero text)

create table usuario( nombre text, idRol integer, pass text, FOREIGN KEY (idRol)  REFERENCES roles(idRol) ON DELETE CASCADE)

create table encuesta (idEncuesta int primary key AUTO_INCREMENT, seriePeli text, saga text, generoPreferido text, numPelis integer, anime integer, valoracion integer, nombreUsu varchar(20), FOREIGN KEY () REFERENCES usuario(nombre) ON DELETE CASCADE);

create table generoUsuario(nombreUsu varchar(20), FOREIGN key (nombreUsu) REFERENCES usuario(nombre) ON DELETE CASCADE,idGenero integer, FOREIGN key (idGenero) REFERENCES generos(idGenero) ON DELETE CASCADE);

create table controlEncuesta (nombreEncuesta varchar(20), activada int);

INSERT INTO controlEncuesta (nombreEncuesta, activada) VALUES ("Cine",1);
INSERT INTO roles (tipoRol) VALUES ("Admin");
INSERT INTO roles (tipoRol) VALUES ("User");
INSERT INTO usuario (`nombre`, `idRol`, `pass`) VALUES ('Salva',  '1', '123456'), ('Mario', '2',  '123456');
INSERT INTO generos (genero) VALUES ("Accion");
INSERT INTO generos (genero) VALUES ("Ciencia Ficcion");
INSERT INTO generos (genero) VALUES ("Romanticas");
alter table usuario add PRIMARY key (nombre);
alter table controlEncuesta add PRIMARY key (nombreEncuesta);
