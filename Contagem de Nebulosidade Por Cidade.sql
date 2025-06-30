SELECT 
	city_name as cidades,
	cloudiness as nebulosidade,
	COUNT(city_name) as Contagem
FROM
	"Clima-AnaliseTemporal"
GROUP BY
	City_name,cloudiness
ORDER BY
	cidades,contagem DESC