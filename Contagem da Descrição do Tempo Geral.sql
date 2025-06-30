SELECT
	description AS descrição,
	COUNT(description) AS contagem
FROM
	"Clima-AnaliseTemporal"
GROUP BY
	descrição 
ORDER BY
	contagem DESC