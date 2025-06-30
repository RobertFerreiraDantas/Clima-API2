SELECT 
	city_name AS cidades,
	humidity AS umidade_porcentagem
FROM
	"Clima-AnaliseTemporal"
ORDER BY
	umidade_porcentagem DESC
LIMIT 10