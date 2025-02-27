WITH age_basket AS (SELECT *, CASE WHEN age >= 20 and age < 30 THEN '20-29'
					WHEN age >= 30 and age < 40 THEN '30-39'
					WHEN age >= 40 and age < 50 THEN '40-49'
					WHEN age >= 50 and age < 60 THEN '50-59'
					WHEN age >= 60 and age < 70 THEN '60-69'
					WHEN age >= 70 and age < 80 THEN '70-79' END as basket_age
					FROM calories)

SELECT basket_age,
ROUND(AVG(height::numeric),2) as average_height,
ROUND(AVG(weight::numeric),2) as average_weight
FROM age_basket
GROUP BY basket_age
ORDER BY basket_age
