-- Trigger que vincula una id de tarjeta y otro de cuenta de banco al usuario creado
DELIMITER //

CREATE TRIGGER antes_de_usuario BEFORE INSERT ON usuario
FOR EACH ROW 
BEGIN
    DECLARE TarjetaId INT;
    DECLARE CuentaId INT;

    INSERT INTO tarjeta_credito (nombre_titular, fecha_expiracion, numero_tarjeta, codigo_ccv) 
    VALUES (NULL, NULL, NULL, '000');

    SET TarjetaId = LAST_INSERT_ID();

    INSERT INTO cuenta_bancaria (numero_cuenta, titular_cuenta, cedula_titular) 
    VALUES ('000000000', '000000000', '000000000');

    SET CuentaId = LAST_INSERT_ID();

    SET NEW.cuenta_banco_id = CuentaId;
    SET NEW.tarjeta_credito_id = TarjetaId;

END;

//

DELIMITER ;


-- TRIGGER CREADO PARA ELIMINAR EL VEHICULO Y SU CONEXION CON EL USUARIO
create trigger ELimiarVehiculo before delete on vehiculo_conductor for each row
	 DELETE FROM vehiculo WHERE vehiculo.id = old.vehiculo_id;

--TRIGGER QUE CAMBIA LA CANTIDAD DE ASIENTOS RESERVADOS EN LA TABLA DE VIAJES AL CREAR UNA RESERVACION DE ASIENTO
create trigger ReservaViaje AFTER insert on reserva_asiento for each row
update viaje set cantidad_pasajeros = cantidad_pasajeros + 1 where new.viaje_id = viaje.id;
