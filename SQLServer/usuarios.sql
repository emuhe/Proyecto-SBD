-- Crear usuarios
CREATE USER 'Derian'@'localhost' IDENTIFIED BY '123';
CREATE USER 'Bryan'@'localhost' IDENTIFIED BY '345';
CREATE USER 'Kiara'@'localhost' IDENTIFIED BY '567';
CREATE USER 'Fernando'@'localhost' IDENTIFIED BY '789';
CREATE USER 'Carolina'@'localhost' IDENTIFIED BY '101';

-- Asignar permisos al procedimiento almacenado
GRANT EXECUTE ON PROCEDURE blablacar.procedure_name TO 'Derian'@'localhost';

-- Asignar permisos a una vista
GRANT SELECT ON blablacar.vista1 TO 'Bryan'@'localhost';

-- Asignar permisos a otra vista
GRANT SELECT ON blablacar.vista2 TO 'Kiara'@'localhost';

-- Asignar permisos a un procedimiento almacenado y una vista para un usuario
GRANT EXECUTE ON PROCEDURE blablacar.procedure_name TO 'Fernando'@'localhost';
GRANT SELECT ON blablacar.vista1 TO 'Fernando'@'localhost';

-- Asignar permisos a un procedimiento almacenado y dos vistas para otro usuario
GRANT EXECUTE ON PROCEDURE blablacar.procedure_name TO 'Carolina'@'localhost';
GRANT SELECT ON blablacar.vista1 TO 'Carolina'@'localhost';
GRANT SELECT ON blablacar.vista2 TO 'Carolina'@'localhost';

-- Creado usuario general
create user 'usuario'@'%' identified by 'userlogin';
GRANT SELECT, INSERT, UPDATE ON blablacar.* TO 'usuario'@'%';
