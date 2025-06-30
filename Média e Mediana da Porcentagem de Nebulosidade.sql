SELECT
	PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY cloudiness) AS mediana_nebulosidade,
	ROUND(AVG(cloudiness)) AS media_nebulosidade
FROM
	"Clima-AnaliseTemporal"