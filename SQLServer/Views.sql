
-- view que sirve para encontrar todos los viajes con sus respectivos datos
create view BuscarViajes as
SELECT 
	c.nombre,c.apellido,v.punto_partida,v.punto_llegada,
	(SELECT count(*) from reserva_asiento ra where viaje_id = v.id),
    v.cantidad_pasajeros,v.precio_por_asiento,v.tiempo_salida,viaje_completado,
    (select avg(val.valoracion) from valoracion val join usuario usr on val.conductor_id = usr.id
    where usr.id = vec.conductor_id),(select vehiculo.modelo from vehiculo where vehiculo.id = vec.vehiculo_id) 
    from viaje v join vehiculo_conductor vec on vec.id = v.vehiculo_conductor_id join usuario c on c.id = vec.conductor_id;

-- View para obtener todos los puntos de partida de todos los viajes
create view Partidas as
 select punto_partida from viaje;
