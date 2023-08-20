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

-- Registros de cada tabla
INSERT INTO cuenta_bancaria (numero_cuenta, titular_cuenta, cedula_titular)
VALUES
  ('12345678901234567890', 'John Doe', '1234567890'),
  ('98765432109876543210', 'Jane Smith', '9876543210'),
  ('55555555555555555555', 'Robert Johnson', '5555555555'),
  ('11111111111111111111', 'Emily White', '1111111111'),
  ('44444444444444444444', 'Michael Brown', '4444444444'),
  ('22222222222222222222', 'David Lee', '2222222222'),
  ('88888888888888888888', 'Sarah Davis', '8888888888'),
  ('33333333333333333333', 'Jessica Wilson', '3333333333'),
  ('66666666666666666666', 'Chris Miller', '6666666666'),
  ('77777777777777777777', 'Jennifer Martinez', '7777777777');

INSERT INTO tarjeta_credito (nombre_titular, fecha_expiracion, numero_tarjeta, codigo_ccv)
VALUES
  ('John Doe', '2025-12-31', '1234567890123456', '123'),
  ('Jane Smith', '2024-09-30', '9876543210987654', '456'),
  ('Robert Johnson', '2023-06-15', '4567890123456789', '789'),
  ('Emily White', '2026-03-20', '7890123456789012', '987'),
  ('Michael Brown', '2024-11-05', '2345678901234567', '654'),
  ('David Lee', '2025-07-18', '3456789012345678', '321'),
  ('Sarah Davis', '2023-04-22', '8901234567890123', '654'),
  ('Jessica Wilson', '2024-01-12', '9012345678901234', '987'),
  ('Chris Miller', '2025-09-05', '5678901234567890', '321'),
  ('Jennifer Martinez', '2023-12-08', '6789012345678901', '654');
  
INSERT INTO usuario (nombre, apellido, preferencia, ruta_foto_perfil, minibiografia, cedula, genero, direccion, fecha_nacimiento, numero_movil, rol, correo_electronico, cuenta_banco_id, tarjeta_credito_id)
VALUES
  ('John', 'Doe', 'Mascotas', 'profile1.jpg', 'Amante de los animales.', '1234567890', 'Masculino', '123 Main St, Ciudad A', '1985-05-10', '5551112233', 'conductor', 'john.doe@example.com', 1, 1),
  ('Jane', 'Smith', 'Fumar', 'profile2.jpg', 'Aventurera y adicta a la adrenalina.', '9876543210', 'Femenino', '456 Oak Ave, Ciudad B', '1990-09-25', '4442221122', 'pasajero', 'jane.smith@example.com', 2, 2),
  ('Robert', 'Johnson', 'Mascotas', 'profile3.jpg', 'Viajero frecuente y amante de la naturaleza.', '5555555555', 'Masculino', '789 Elm St, Ciudad C', '1988-12-02', '3338889911', 'conductor', 'robert.johnson@example.com', 3, 3),
  ('Emily', 'White', 'Coversacion', 'profile4.jpg', 'Aficionada a la música y la cultura.', '1111111111', 'Femenino', '101 Pine Ave, Ciudad D', '1992-03-15', '6667771122', 'pasajero', 'emily.white@example.com', 4, 4),
  ('Michael', 'Brown', 'Mascotas', 'profile5.jpg', 'Amante de los animales y conductor experimentado.', '4444444444', 'Masculino', '222 Cedar St, Ciudad E', '1979-11-20', '5556668877', 'conductor', 'michael.brown@example.com', 5, 5),
  ('David', 'Lee', 'Musica', 'profile6.jpg', 'Melómano y aficionado a los conciertos.', '2222222222', 'Masculino', '333 Birch Rd, Ciudad F', '1993-07-05', '9997772233', 'pasajero', 'david.lee@example.com', 6, 6),
  ('Sarah', 'Davis', 'Mascotas', 'profile7.jpg', 'Amante de los animales y la naturaleza.', '8888888888', 'Femenino', '444 Oakwood Dr, Ciudad G', '1984-04-12', '3335556677', 'conductor', 'sarah.davis@example.com', 7, 7),
  ('Jessica', 'Wilson', 'Fumar', 'profile8.jpg', 'Viajera empedernida y aventurera.', '3333333333', 'Femenino', '555 Maple St, Ciudad H', '1991-01-28', '2228881166', 'pasajero', 'jessica.wilson@example.com', 8, 8),
  ('Chris', 'Miller', 'Musica', 'profile9.jpg', 'Melómano y aficionado a la música en vivo.', '6666666666', 'Masculino', '666 Walnut Ln, Ciudad I', '1987-09-10', '7775559988', 'conductor', 'chris.miller@example.com', 9, 9),
  ('Jennifer', 'Martinez', 'Coversacion', 'profile10.jpg', 'Apasionada de la cultura y la historia.', '7777777777', 'Femenino', '777 Elmwood Ave, Ciudad J', '1995-12-18', '8883337744', 'pasajero', 'jennifer.martinez@example.com', 10, 10);

INSERT INTO vehiculo (modelo, marca, fecha_matricula, tipo_vehiculo, color, placa, activo)
VALUES
  ('Chevrolet Cruze', 'Chevrolet', '2020-06-25', 'Sedán', 'Azul', 'JKL4567', 1),
  ('Nissan Rogue', 'Nissan', '2019-09-14', 'SUV', 'Plateado', 'MNO7890', 1),
  ('Toyota RAV4', 'Toyota', '2021-02-10', 'SUV', 'Blanco', 'PQR1234', 1),
  ('Ford Focus', 'Ford', '2020-04-30', 'Sedán', 'Negro', 'STU5678', 1),
  ('Honda CR-V', 'Honda', '2021-08-18', 'SUV', 'Rojo', 'VWX9012', 1),
  ('Hyundai Sonata', 'Hyundai', '2022-03-22', 'Sedán', 'Gris', 'YZA3456', 1),
  ('Mazda CX-5', 'Mazda', '2021-11-05', 'SUV', 'Azul Oscuro', 'BCD6789', 1),
  ('Volkswagen Jetta', 'Volkswagen', '2020-07-11', 'Sedán', 'Plata', 'EFG9012', 1),
  ('Kia Sorento', 'Kia', '2022-06-30', 'SUV', 'Blanco Perla', 'HIJ2345', 1),
  ('Chevrolet Equinox', 'Chevrolet', '2021-05-28', 'SUV', 'Negro', 'KLM5678', 1);

INSERT INTO vehiculo_conductor (vehiculo_id, conductor_id)
VALUES
  (1, 1),
  (2, 3),
  (3, 5),
  (4, 2),
  (5, 4),
  (6, 6), 
  (7, 7), 
  (8, 8), 
  (9, 9),
  (10, 10);

INSERT INTO viaje (vehiculo_conductor_id, cantidad_pasajeros, precio_por_asiento, punto_partida, punto_llegada, tiempo_salida, viaje_completado)
VALUES
  (1, 3, 25.50, 'Guayaquil', 'Cuenca', '2023-08-15 10:00:00', 0), 
  (2, 2, 20.00, 'Santo Domingo', 'Quito', '2023-08-20 08:30:00', 0), 
  (3, 1, 15.75, 'Durán', 'Portoviejo', '2023-08-18 14:45:00', 1), 
  (1, 4, 18.25, 'Loja', 'Ambato', '2023-08-22 12:00:00', 0), 
  (4, 2, 22.75, 'Esmeraldas', 'Guayaquil', '2023-08-17 09:15:00', 0),
  (5, 3, 30.00, 'Milagro', ' Babahoyo', '2023-08-23 11:30:00', 1), 
  (6, 1, 12.50, 'Daule', 'Huaquillas', '2023-08-21 16:20:00', 0), 
  (7, 4, 19.80, 'Jipijapa', 'Ventanas', '2023-08-19 13:45:00', 0), 
  (8, 2, 24.75, 'El Triunfo', 'Salinas', '2023-08-25 10:30:00', 0), 
  (9, 3, 26.00, 'Salinas', 'Guayaquil', '2023-08-24 09:00:00', 1); 

INSERT INTO reserva_asiento (viaje_id, pasajero_id)
VALUES
  (1, 2), 
  (1, 4),
  (3, 5),
  (4, 1), 
  (2, 3), 
  (5, 7), 
  (6, 9), 
  (7, 6), 
  (8, 10),
  (9, 8);

INSERT INTO pagos (viaje_id, pasajero_id, monto_pagado, metodo_pago, tarjeta_pago_id, cuenta_deposito_id, fecha_pago)
VALUES
  (1, 2, 50.00, 'Tarjeta de crédito', 2, NULL, '2023-08-13 15:30:00'),
  (1, 4, 25.50, 'Tarjeta de crédito', 4, NULL, '2023-08-13 16:00:00'),
  (3, 5, 15.75, 'Tarjeta de crédito', 5, NULL, '2023-08-17 10:45:00'),
  (4, 1, 18.25, 'Depósito bancario', NULL, 1, '2023-08-20 11:00:00'),
  (2, 3, 40.00, 'Tarjeta de crédito', 3, NULL, '2023-08-19 08:30:00'),
  (5, 7, 90.00, 'Depósito bancario', NULL, 3, '2023-08-22 14:15:00'),
  (6, 9, 12.50, 'Tarjeta de crédito', 6, NULL, '2023-08-21 16:30:00'),
  (7, 6, 79.20, 'Tarjeta de crédito', 7, NULL, '2023-08-19 14:00:00'),
  (8, 10, 74.25, 'Tarjeta de crédito', 8, NULL, '2023-08-25 10:45:00'),
  (9, 8, 78.00, 'Depósito bancario', NULL, 2, '2023-08-24 09:30:00');

INSERT INTO valoracion (viaje_id, pasajero_id, conductor_id, valoracion, fecha_valoracion)
VALUES
  (1, 2, 3, '4', '2023-08-15'),
  (1, 4, 3, '5', '2023-08-15'),
  (3, 5, 6, '3', '2023-08-18'),
  (4, 1, 7, '4', '2023-08-20'),
  (2, 3, 8, '5', '2023-08-19'),
  (5, 7, 9, '4', '2023-08-23'),
  (6, 9, 10, '3', '2023-08-21'),
  (7, 6, 3, '5', '2023-08-19'),
  (8, 10, 5, '4', '2023-08-25'),
  (9, 8, 2, '5', '2023-08-24');

INSERT INTO conversacion (fecha_inicio, conductor_id, pasajero_id)
VALUES
  ('2023-08-15 14:30:00', 3, 2),
  ('2023-08-15 16:45:00', 3, 4),
  ('2023-08-18 11:15:00', 6, 5),
  ('2023-08-20 10:30:00', 7, 1),
  ('2023-08-19 09:30:00', 8, 3),
  ('2023-08-23 13:20:00', 9, 7),
  ('2023-08-21 15:00:00', 10, 9),
  ('2023-08-19 17:45:00', 3, 6),
  ('2023-08-25 12:30:00', 5, 10),
  ('2023-08-24 08:00:00', 2, 8);

INSERT INTO mensaje (conversacion_id, emisor_id, mensaje, fecha_envio)
VALUES
  (1, 3, 'Hola, ¿a qué hora saldremos mañana?', '2023-08-15 14:35:00'),
  (1, 2, 'Hola, saldremos a las 8:00 AM.', '2023-08-15 14:40:00'),
  (2, 3, 'Hola, ¿cómo estás?', '2023-08-15 16:50:00'),
  (2, 4, '¡Hola! Estoy bien, ¿y tú?', '2023-08-15 16:55:00'),
  (3, 6, 'Hola, ya casi llego al punto de encuentro.', '2023-08-18 11:20:00'),
  (3, 5, 'Perfecto, te estaré esperando.', '2023-08-18 11:25:00'),
  (4, 7, '¿Podrías llevar una maleta pequeña?', '2023-08-20 10:35:00'),
  (4, 1, 'Claro, no hay problema.', '2023-08-20 10:40:00'),
  (5, 8, 'Gracias por el viaje, fue genial.', '2023-08-19 09:35:00'),
  (5, 3, 'Me alegra que te haya gustado. ¡Hasta la próxima!', '2023-08-19 09:40:00');

INSERT INTO opinion (viaje_id, pasajero_id, conductor_id, descripcion, fecha_opinion)
VALUES
  (1, 2, 3, 'El viaje estuvo cómodo y seguro.', '2023-08-15'),
  (1, 4, 3, 'El conductor fue muy amable y puntual.', '2023-08-15'),
  (3, 5, 6, 'El viaje se retrasó un poco debido al tráfico.', '2023-08-18'),
  (4, 1, 7, 'Muy buena experiencia, el conductor fue profesional.', '2023-08-20'),
  (2, 3, 8, 'El vehículo estaba limpio y cómodo.', '2023-08-19'),
  (5, 7, 9, 'El conductor fue muy simpático y atento.', '2023-08-23'),
  (6, 9, 10, 'Me gustó la música que tenía el conductor en el viaje.', '2023-08-21'),
  (7, 6, 3, 'Excelente servicio, lo recomiendo.', '2023-08-19'),
  (8, 10, 5, 'El conductor condujo con seguridad.', '2023-08-25'),
  (9, 8, 2, 'Fue un viaje muy tranquilo y agradable.','2023-08-24');


-- CONSULTAS --
-- 1. Consulta para ver los viajes realizados por un conductor de id=2
SELECT v.id AS viaje_id, v.punto_partida, v.punto_llegada, val.valoracion, op.descripcion AS opinion
FROM viaje v
LEFT JOIN valoracion val ON v.id = val.viaje_id AND val.conductor_id = 2
LEFT JOIN opinion op ON v.id = op.viaje_id AND op.conductor_id = 2
WHERE v.vehiculo_conductor_id = (
    SELECT id FROM vehiculo_conductor WHERE conductor_id = 2
);

-- 2. Consulta para ver el promedio de las valoraciones de cada conductor
SELECT c.id AS conductor_id, c.nombre AS nombre_conductor, c.apellido AS apellido_conductor, AVG(v.valoracion) AS promedio_valoracion
FROM usuario c
LEFT JOIN valoracion v ON c.id = v.conductor_id
WHERE c.rol = 'conductor'
GROUP BY c.id, c.nombre, c.apellido;

-- 3. Consulta para ver viajes con sus respectivo conductor y vehiculo
SELECT v.id AS viaje_id, v.punto_partida, v.punto_llegada, vehiculo.*, u.nombre AS nombre_conductor, u.apellido AS apellido_conductor
FROM viaje v
INNER JOIN vehiculo_conductor vc ON v.vehiculo_conductor_id = vc.id
INNER JOIN vehiculo ON vc.vehiculo_id = vehiculo.id
INNER JOIN usuario u ON vc.conductor_id = u.id;

-- 4. Consulta para ver una conversacion
SELECT m.*, u.nombre AS nombre_emisor
FROM mensaje m
INNER JOIN usuario u ON m.emisor_id = u.id
WHERE m.conversacion_id = 5
ORDER BY m.fecha_envio;

-- 5. Consulta para ver pagos realizados por un usuario
SELECT p.*, v.punto_partida, v.punto_llegada, v.tiempo_salida, u.nombre AS nombre_pasajero
FROM pagos p
INNER JOIN viaje v ON p.viaje_id = v.id
INNER JOIN usuario u ON p.pasajero_id = u.id
WHERE p.pasajero_id = 5
ORDER BY p.fecha_pago;

-- 6. Consulta para ver viajes no completados por un conductor
SELECT v.id AS viaje_id, v.punto_partida, v.punto_llegada, v.tiempo_salida
FROM viaje v
INNER JOIN vehiculo_conductor vc ON v.vehiculo_conductor_id = vc.id
WHERE vc.conductor_id = 2 AND v.viaje_completado = 0;

-- 7. Consulta para ver numero de viajes de pasajero id=6
SELECT COUNT(*) AS num_viajes_pasajero
FROM reserva_asiento
WHERE pasajero_id = 6;

-- 8. Consulta para ver el numero asientos disponibles en un viaje
SELECT v.id AS viaje_id, v.cantidad_pasajeros - COUNT(ra.id) AS asientos_disponibles
FROM viaje v
LEFT JOIN reserva_asiento ra ON v.id = ra.viaje_id
WHERE v.id = 4
GROUP BY v.id, v.cantidad_pasajeros;
