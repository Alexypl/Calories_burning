SELECT gender,
ROUND(AVG(CAST(calories as numeric)), 2) as average_calories_by_gender
FROM calories
GROUP BY gender
