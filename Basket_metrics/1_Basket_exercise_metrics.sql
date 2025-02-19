WITH age_basket AS (SELECT *, CASE WHEN age >= 20 and age < 30 THEN '20-29'
					WHEN age >= 30 and age < 40 THEN '30-39'
					WHEN age >= 40 and age < 50 THEN '40-49'
					WHEN age >= 50 and age < 60 THEN '50-59'
					WHEN age >= 60 and age < 70 THEN '60-69'
					WHEN age >= 70 and age < 80 THEN '70-79' END as basket_age
					FROM calories)

SELECT basket_age,
ROUND(AVG(duration::numeric),2) as average_duration,
ROUND(AVG(heart_rate::numeric),2) as average_heart_rate,
ROUND(AVG(body_temp::numeric),2) as average_body_temp
FROM age_basket
GROUP BY basket_age
ORDER BY basket_age
