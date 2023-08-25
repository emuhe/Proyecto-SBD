
-- Se consiguen todos los puntos de llegada segun el destino
DELIMITER %%
	Create procedure BuscarViaje (in partida varchar(100))
    BEGIN
    SELECT punto_llegada from viaje where punto_partida = partida;
    END %%
-- Se consiguen los datos de los viajes dependiendo del destino y partida escogido (si no se ha escogido entonces muestra todos)
DELIMITER %%
create procedure FiltrarViaje (in partida varchar(100), in llegada varchar(100))
BEGIN 
IF llegada = '-Todos-' and partida = '-Todos-' then
SELECT
	c.nombre,c.apellido,v.punto_partida,v.punto_llegada,
	(SELECT count(*) from reserva_asiento ra where viaje_id = v.id),
    v.cantidad_pasajeros,v.precio_por_asiento,v.tiempo_salida,viaje_completado,
    (select avg(val.valoracion) from valoracion val join usuario usr on val.conductor_id = usr.id
    where usr.id = vec.conductor_id),(select vehiculo.modelo from vehiculo where vehiculo.id = vec.vehiculo_id) 
    from viaje v join vehiculo_conductor vec on vec.id = v.vehiculo_conductor_id join usuario c on c.id = vec.conductor_id;
elseif llegada = '-Todos-' and partida <> '-Todos-' then
SELECT
	c.nombre,c.apellido,v.punto_partida,v.punto_llegada,
	(SELECT count(*) from reserva_asiento ra where viaje_id = v.id),
    v.cantidad_pasajeros,v.precio_por_asiento,v.tiempo_salida,viaje_completado,
    (select avg(val.valoracion) from valoracion val join usuario usr on val.conductor_id = usr.id
    where usr.id = vec.conductor_id),(select vehiculo.modelo from vehiculo where vehiculo.id = vec.vehiculo_id) 
    from viaje v join vehiculo_conductor vec on vec.id = v.vehiculo_conductor_id join usuario c on c.id = vec.conductor_id where v.punto_partida = partida;
elseif llegada <> '-Todos-' and partida = '-Todos-' then
SELECT
	c.nombre,c.apellido,v.punto_partida,v.punto_llegada,
	(SELECT count(*) from reserva_asiento ra where viaje_id = v.id),
    v.cantidad_pasajeros,v.precio_por_asiento,v.tiempo_salida,viaje_completado,
    (select avg(val.valoracion) from valoracion val join usuario usr on val.conductor_id = usr.id
    where usr.id = vec.conductor_id),(select vehiculo.modelo from vehiculo where vehiculo.id = vec.vehiculo_id) 
    from viaje v join vehiculo_conductor vec on vec.id = v.vehiculo_conductor_id join usuario c on c.id = vec.conductor_id where v.punto_llegada = llegada;
else
SELECT
	c.nombre,c.apellido,v.punto_partida,v.punto_llegada,
	(SELECT count(*) from reserva_asiento ra where viaje_id = v.id),
    v.cantidad_pasajeros,v.precio_por_asiento,v.tiempo_salida,viaje_completado,
    (select avg(val.valoracion) from valoracion val join usuario usr on val.conductor_id = usr.id
    where usr.id = vec.conductor_id),(select vehiculo.modelo from vehiculo where vehiculo.id = vec.vehiculo_id) 
    from viaje v join vehiculo_conductor vec on vec.id = v.vehiculo_conductor_id join usuario c on c.id = vec.conductor_id where v.punto_partida = partida and v.punto_llegada = llegada;
end if;
end
%%

-- Procedure par aobtener todos los puntos de destino segun el punto de partida (si es todos entonces retorna todos)
DELIMITER $$
create procedure obtenerLlegadas (in partida varchar(100))
BEGIN
IF partida = '-Todos-' then
SELECT punto_llegada from viaje;
else
SELECT punto_llegada from viaje where punto_partida = partida;
end if;
end
$$

-- Procedure para crear un vehiculo y que tambien se cree una conexion con vehiculo_Conductor. se utilizan transacciones y rollbacks
DELIMITER //
CREATE PROCEDURE InsertIntoVehiculoAndVehiculoConductor(
    IN p_id INT, IN p_modelo VARCHAR(255), IN p_marca VARCHAR(255), IN p_fecha_matricula DATE,
    IN p_tipo_vehiculo VARCHAR(255), IN p_color VARCHAR(255), IN p_placa VARCHAR(255), 
    IN p_activo BOOLEAN, IN p_conductor_id INT)
BEGIN
    DECLARE v_veh_id INT;
    DECLARE v_error_occurred INT DEFAULT 0;
    
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
        SET v_error_occurred = 1;
    END;

    START TRANSACTION;

    INSERT INTO VEHICULO (id, modelo, marca, fecha_matricula, tipo_vehiculo, color, placa, activo)
    VALUES (p_id, p_modelo, p_marca, p_fecha_matricula, p_tipo_vehiculo, p_color, p_placa, p_activo);
    
    SET v_veh_id = LAST_INSERT_ID();

    INSERT INTO VEHICULO_CONDUCTOR (vehiculo_id, conductor_id)
    VALUES (v_veh_id, p_conductor_id);

    IF v_error_occurred = 1 THEN
        ROLLBACK;
    ELSE
        COMMIT;
    END IF;

END;
//
DELIMITER ;
