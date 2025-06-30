SELECT
	city_name AS cidades,
	AVG(rain) AS media_chuva,
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY rain) AS mediana_chuva
FROM
	"Clima-AnaliseTemporal"
GROUP BY
	cidades