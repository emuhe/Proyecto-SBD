
-- Se consiguen todos los puntos de llegada segun el destino
DELIMITER %%
	Create procedure BuscarViaje (in partida varchar(100))
    BEGIN
    SELECT punto_llegada from viaje where punto_partida = partida;
    END %%
-- Se consiguen los datos de los viajes dependiendo del destino escogido (si no se ha escogido entonces muestra todos)
DELIMITER %%
create procedure FiltrarViaje (in partida varchar(100), in llegada varchar(100))
BEGIN 
IF llegada = '-Todos-' then
SELECT
	c.nombre,c.apellido,v.punto_partida,v.punto_llegada,
	(SELECT count(*) from reserva_asiento ra where viaje_id = v.id),
    v.cantidad_pasajeros,v.precio_por_asiento,v.tiempo_salida,viaje_completado,
    (select avg(val.valoracion) from valoracion val join usuario usr on val.conductor_id = usr.id
    where usr.id = vec.conductor_id),(select vehiculo.modelo from vehiculo where vehiculo.id = vec.vehiculo_id) 
    from viaje v join vehiculo_conductor vec on vec.id = v.vehiculo_conductor_id join usuario c on c.id = vec.conductor_id where v.punto_partida = partida;
ELSE
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
