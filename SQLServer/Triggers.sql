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

    SET NEW.cuenta_banco_id = lastCuentaId;
    SET NEW.tarjeta_credito_id = lastTarjetaId;

END;

//

DELIMITER ;
