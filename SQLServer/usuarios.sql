-- Crear usuarios
CREATE USER 'Derian'@'localhost' IDENTIFIED BY '123';
CREATE USER 'Bryan'@'localhost' IDENTIFIED BY '345';
CREATE USER 'Kiara'@'localhost' IDENTIFIED BY '567';
CREATE USER 'Fernando'@'localhost' IDENTIFIED BY '789';
CREATE USER 'Carolina'@'localhost' IDENTIFIED BY '101';

-- Asignar permisos al procedimiento almacenado y una vista
GRANT EXECUTE ON PROCEDURE blablacar.obtenerLlegadas TO 'Derian'@'localhost';
GRANT SELECT ON blablacar.vista_info_conductores TO 'Derian'@'localhost';
FLUSH PRIVILEGES;

-- Asignar permisos a una vista
GRANT SELECT ON blablacar.BuscarViajes  TO 'Bryan'@'localhost';
FLUSH PRIVILEGES;

-- Asignar permisos a otras vistas 
GRANT SELECT ON blablacar.Partidas TO 'Kiara'@'localhost';
GRANT SELECT ON blablacar.vista_info_conductores TO 'Kiara'@'localhost';
FLUSH PRIVILEGES;

-- Asignar permisos a un procedimiento almacenado y una vista para un usuario
GRANT EXECUTE ON PROCEDURE blablacar.BuscarViaje TO 'Fernando'@'localhost';
GRANT SELECT ON blablacar.BuscarViajes TO 'Fernando'@'localhost';
FLUSH PRIVILEGES;

-- Asignar permisos a un procedimiento almacenado y dos vistas para otro usuario
GRANT EXECUTE ON PROCEDURE blablacar.FiltrarViaje TO 'Carolina'@'localhost';
GRANT SELECT ON blablacar.BuscarViajes TO 'Carolina'@'localhost';
GRANT SELECT ON blablacar.Partidas TO 'Carolina'@'localhost';
FLUSH PRIVILEGES;

-- Asignar permisos procedimiento almacenado  para otro usuario
GRANT EXECUTE ON PROCEDURE blablacar.InsertIntoVehiculoAndVehiculoConductor TO 'Bryan'@'localhost';
GRANT EXECUTE ON PROCEDURE blablacar.obtenerLlegadas TO 'Bryan'@'localhost';
GRANT EXECUTE ON PROCEDURE blablacar.ReservarViaje TO 'Bryan'@'localhost';
FLUSH PRIVILEGES;

-- Creado usuario general
create user 'usuario'@'%' identified by 'userlogin';
GRANT SELECT, INSERT, UPDATE ON blablacar.* TO 'usuario'@'%';
FLUSH PRIVILEGES;
