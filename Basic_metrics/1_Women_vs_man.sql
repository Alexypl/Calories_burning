SELECT gender, 
ROUND(AVG(age), 2) as average_age,
ROUND(AVG(CAST(height as numeric)),2) as average_height,
ROUND(AVG(CAST(weight as numeric)),2) as average_weight
FROM calories
GROUP BY gender
