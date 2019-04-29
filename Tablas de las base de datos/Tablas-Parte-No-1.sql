/********************
Creacion de las tablas
*********************/

CREATE TABLE  Product(
  maker VARCHAR(30) NOT NULL,
  model VARCHAR(30) NOT NULL,
  type VARCHAR(30) NOT NULL,
  PRIMARY KEY (maker)
);

CREATE TABLE PC(
  model VARCHAR(30) NOT NULL,
  speed VARCHAR(30) NOT NULL,
  ram VARCHAR(30) NOT NULL,
  hd  VARCHAR(30) NOT NULL,
  price FLOAT NOT NULL,
  PRIMARY KEY (model)
);

CREATE TABLE Laptop(
  model VARCHAR(30) NOT NULL,
  speed VARCHAR(30) NOT NULL,
  ram VARCHAR(30) NOT NULL,
  hd VARCHAR(30) NOT NULL,
  screen VARCHAR(30) NOT NULL,
  price FLOAT NOT NULL,
  PRIMARY KEY (model)
);

CREATE TABLE Printer(
  model VARCHAR(30) NOT NULL,
  color VARCHAR(30) NOT NULL,
  type VARCHAR(30) NOT NULL,
  price fLOAT NOT NULL,
  PRIMARY KEY (model)
);
