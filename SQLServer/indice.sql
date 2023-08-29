-- creados para agilitar la filtracion de viajes 
CREATE INDEX IndicePartida ON viaje (punto_partida);

CREATE INDEX IndiceLlegada ON viaje (punto_llegada);
