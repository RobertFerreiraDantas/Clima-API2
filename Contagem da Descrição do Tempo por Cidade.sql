SELECT
	city_name AS cidades
	,description AS descrição
	,COUNT(description) AS Contagem
FROM
	"Clima-AnaliseTemporal"
GROUP BY
	city_name,description
ORDER BY 
	cidades,contagem DESC