DELIMITER %%
	Create procedure BuscarViaje (in partida varchar(100))
    BEGIN
    SELECT punto_llegada from viaje where punto_partida = partida;
    END %%
