
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

-- View para obtener un historial completos de los viajes
CREATE VIEW historial_viajes_completo 
AS	SELECT v.id AS viaje_id, v.punto_partida, v.punto_llegada, v.tiempo_salida, u.nombre AS nombre_conductor, ve.modelo AS modelo_vehiculo, ve.marca AS marca_vehiculo, va.valoracion AS valoracion_pasajero, va.fecha_valoracion
	FROM viaje v
	JOIN vehiculo_conductor vc ON v.vehiculo_conductor_id = vc.id
	JOIN usuario u ON vc.conductor_id = u.id
	JOIN vehiculo ve ON vc.vehiculo_id = ve.id
	LEFT JOIN valoracion va ON v.id = va.viaje_id;



-- View para mostrar información sobre los conductores y la cantidad promedio de valoraciones que han recibido.
CREATE VIEW vista_info_conductores AS
SELECT
    u.id AS conductor_id,
    u.nombre AS nombre_conductor,
    u.apellido AS apellido_conductor,
    u.genero AS genero_conductor,
    u.fecha_nacimiento AS fecha_nacimiento_conductor,
    COUNT(v.id) AS cantidad_viajes_realizados,
    AVG(val.valoracion) AS promedio_valoraciones
FROM usuario AS u
LEFT JOIN vehiculo_conductor AS vc ON u.id = vc.conductor_id
LEFT JOIN viaje AS v ON vc.id = v.vehiculo_conductor_id
LEFT JOIN valoracion AS val ON u.id = val.conductor_id
WHERE u.rol = 'conductor'
GROUP BY u.id, u.nombre, u.apellido, u.genero, u.fecha_nacimiento;
