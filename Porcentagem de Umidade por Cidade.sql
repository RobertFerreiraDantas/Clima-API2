WITH tabela1 AS (
	SELECT
		city_name as cidades,
		humidity as umidade_porcentagem,
		CASE
			WHEN humidity > 70 THEN 'ALTO'
			ELSE 'DESPREZÍVEL'
		END AS "refinamento"
	FROM
		"Clima-AnaliseTemporal"
)
SELECT 
	cidades,refinamento,COUNT(refinamento) as contagem
FROM 
	tabela1 
WHERE
	refinamento='ALTO'
GROUP BY
	cidades,refinamento
ORDER BY
	contagem DESC

