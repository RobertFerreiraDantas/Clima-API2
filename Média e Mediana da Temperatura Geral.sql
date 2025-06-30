SELECT
	ROUND(AVG("temp")) as média_temperatura,
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY "temp") AS mediana_temperatura
FROM
	"Clima-AnaliseTemporal"