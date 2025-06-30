WITH tabela1 AS(
	SELECT
		date_trunc('hour',time::time) AS tempo_normalizado,
		(cloudiness::int/10)*10 AS nebulosidade_normalizada,
		("temp"/10)*10 AS temperatura_normalizado,
		(humidity::int/10)*10 AS umidade_normalizada,
		CASE
			WHEN time::time >= '00:00' AND time::time < '12:00' THEN 'Manhã'
		    WHEN time::time >= '12:00' AND time::time < '18:00' THEN 'Tarde'
		    ELSE 'Noite'
		END AS turno
	FROM
		"Clima-AnaliseTemporal"
	
)
SELECT
	 turno,
	 nebulosidade_normalizada AS nebulosidade_normalizada,
	 COUNT(nebulosidade_normalizada) AS contagem
FROM
	tabela1
GROUP BY
	turno,
	 nebulosidade_normalizada
ORDER BY
	turno,
	contagem DESC