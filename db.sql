CREATE DATABASE IF NOT EXISTS prueba1;
USE prueba1;

CREATE TABLE IF NOT EXISTS autos(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    marca VARCHAR(50) 
)