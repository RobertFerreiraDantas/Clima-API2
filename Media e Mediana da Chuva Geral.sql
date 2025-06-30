SELECT
	AVG(rain) as media_chuva,
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY rain) AS mediana_chuva
FROM
	"Clima-AnaliseTemporal"