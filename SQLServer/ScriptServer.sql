CREATE DATABASE blablacar;
use blablacar;

-- Tabla de cuentas bancarias
CREATE TABLE IF NOT EXISTS cuenta_bancaria (
  id INT AUTO_INCREMENT PRIMARY KEY,
  numero_cuenta VARCHAR(24) NOT NULL,
  titular_cuenta VARCHAR(50) NOT NULL,
  cedula_titular VARCHAR(10) NOT NULL
);

-- Tabla de tarjetas de crédito
CREATE TABLE IF NOT EXISTS tarjeta_credito (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre_titular varchar(50),
  fecha_expiracion DATE,
  numero_tarjeta varchar(16),
  codigo_ccv VARCHAR(3) NOT NULL
);

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuario (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL,
  preferencia  ENUM('Fumar','Mascotas','Coversacion','Musica'),
  ruta_foto_perfil VARCHAR(255),
  minibiografia VARCHAR(200), 
  cedula VARCHAR(10) NOT NULL,
  genero ENUM('Femenino','Masculino'),
  direccion VARCHAR(200) NOT NULL,
  fecha_nacimiento DATE NOT NULL,
  numero_movil VARCHAR(10) NOT NULL,
  rol ENUM('conductor', 'pasajero') NOT NULL,
  correo_electronico VARCHAR(50),
  cuenta_banco_id INT,
  tarjeta_credito_id INT,
  FOREIGN KEY (cuenta_banco_id) REFERENCES cuenta_bancaria(id),
  FOREIGN KEY (tarjeta_credito_id) REFERENCES tarjeta_credito(id)
);

-- Tabla de vehiculos
CREATE TABLE IF NOT EXISTS vehiculo (
  id INT AUTO_INCREMENT PRIMARY KEY,
  modelo VARCHAR(50) NOT NULL,
  marca VARCHAR(50) NOT NULL,
  fecha_matricula DATE NOT NULL, 
  tipo_vehiculo VARCHAR(30) NOT NULL,
  color VARCHAR(20) NOT NULL, 
  placa VARCHAR(8) NOT NULL,
  activo BOOLEAN DEFAULT 1 -- Campo para indicar si el vehículo está activo (1) o desactivado (0)
);

-- Tabla de relacion entre vehiculo y conductor
CREATE TABLE IF NOT EXISTS vehiculo_conductor (
  id INT AUTO_INCREMENT PRIMARY KEY,
  vehiculo_id INT NOT NULL,
  conductor_id INT NOT NULL,
  FOREIGN KEY (vehiculo_id) REFERENCES vehiculo(id),
  FOREIGN KEY (conductor_id) REFERENCES usuario(id)
);

-- Tabla de viajes
CREATE TABLE IF NOT EXISTS viaje (
  id INT AUTO_INCREMENT PRIMARY KEY,
  vehiculo_conductor_id INT NOT NULL,
  cantidad_pasajeros INT NOT NULL,
  precio_por_asiento DECIMAL(10, 2) NOT NULL,
  punto_partida VARCHAR(100) NOT NULL,
  punto_llegada VARCHAR(100) NOT NULL,
  tiempo_salida DATETIME NOT NULL,
  viaje_completado BOOLEAN DEFAULT 0,
  FOREIGN KEY (vehiculo_conductor_id) REFERENCES vehiculo_conductor(id)
);

-- Tabla de reservas de asientos
CREATE TABLE IF NOT EXISTS reserva_asiento(
  id INT AUTO_INCREMENT PRIMARY KEY,
  viaje_id INT NOT NULL,
  pasajero_id INT NOT NULL,
  FOREIGN KEY (viaje_id) REFERENCES viaje(id),
  FOREIGN KEY (pasajero_id) REFERENCES usuario(id)
);

-- Tabla de pagos
CREATE TABLE IF NOT EXISTS pagos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  viaje_id INT NOT NULL,
  pasajero_id INT NOT NULL,
  monto_pagado DECIMAL(10, 2) NOT NULL,
  metodo_pago VARCHAR(50) NOT NULL,
  tarjeta_pago_id INT,
  cuenta_deposito_id INT,
  fecha_pago DATETIME NOT NULL,
  FOREIGN KEY (viaje_id) REFERENCES viaje(id),
  FOREIGN KEY (pasajero_id) REFERENCES usuario(id),
  FOREIGN KEY (tarjeta_pago_id) REFERENCES tarjeta_credito(id),
  FOREIGN KEY (cuenta_deposito_id) REFERENCES cuenta_bancaria(id)
);

-- Tabla de valoraciones
CREATE TABLE IF NOT EXISTS valoracion (
  id INT AUTO_INCREMENT PRIMARY KEY,
  viaje_id INT NOT NULL,
  pasajero_id INT NOT NULL,
  conductor_id INT NOT NULL,
  valoracion ENUM ('1','2','3','4','5'),
  fecha_valoracion DATE NOT NULL,
  FOREIGN KEY (viaje_id) REFERENCES viaje(id),
  FOREIGN KEY (pasajero_id) REFERENCES usuario(id),
  FOREIGN KEY (conductor_id) REFERENCES usuario(id)
);

-- Tabla de conversaciones
CREATE TABLE IF NOT EXISTS conversacion (
  id INT AUTO_INCREMENT PRIMARY KEY,
  fecha_inicio DATETIME NOT NULL,
  conductor_id INT NOT NULL,
  pasajero_id INT NOT NULL,
  FOREIGN KEY (conductor_id) REFERENCES usuario(id),
  FOREIGN KEY (pasajero_id) REFERENCES usuario(id)
);

-- Tabla de mensajes
CREATE TABLE IF NOT EXISTS mensaje (
  id INT AUTO_INCREMENT PRIMARY KEY,
  conversacion_id INT NOT NULL,
  emisor_id INT NOT NULL,
  mensaje VARCHAR(255) NOT NULL,
  fecha_envio DATETIME NOT NULL,
  FOREIGN KEY (conversacion_id) REFERENCES conversacion(id),
  FOREIGN KEY (emisor_id) REFERENCES usuario(id)
);

-- Tabla de opiniones
CREATE TABLE IF NOT EXISTS opinion (
  id INT AUTO_INCREMENT PRIMARY KEY,
  viaje_id INT NOT NULL,
  pasajero_id INT NOT NULL,
  conductor_id INT NOT NULL,
  descripcion VARCHAR(255), 
  fecha_opinion DATE NOT NULL,
  FOREIGN KEY (viaje_id) REFERENCES viaje(id),
  FOREIGN KEY (conductor_id) REFERENCES usuario(id),
  FOREIGN KEY (pasajero_id) REFERENCES usuario(id)
);
