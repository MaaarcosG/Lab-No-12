/*
 Universidad del Valle de Guatemala
 Base de Datos
	Marcos Gutierrez
	17909
 Database: Lab-No-12
*/

/**
EXAMPLE TO REFERENCE
  CREATE DATABASE yourdbname;
  CREATE USER youruser WITH ENCRYPTED PASSWORD 'yourpass';
  GRANT ALL PRIVILEGES ON DATABASE yourdbname TO youruser;

  link: https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e
**/

-- Creamos los usuarios A-C
CREATE USER operador PASSWORD 'operador';
Create User gerente password 'gerente';
Create user administrador password 'admin';
Grant connect on database lab11 to administrador, operador, gerente;

-- Asignacion de los permisos incisio D
Grant All privileges on Database postgres To administrador with grant option;
Grant All privileges on All tables in SCHEMA public To administrador with Grant option;

-- Asignacion de los lectura en las tablas al operador
Grant Select on All tables in Schema public to operador;

-- Asignacion solo lectura y escritura al gerente
Grant Select, Insert on All tables in schema public to gerente;

-- Permiso de creacion de objetos al usuario gerente
Grant Create on database lab11 to gerente;

-- Permiso de creacion de llaves foraneas y disparadoras al usuario
Revoke References, Trigger on All Tables in Schema public from operador;
