SELECT gender, 
ROUND(AVG(CAST(duration as numeric)), 2) as average_duration_by_gender,
ROUND(AVG(CAST(heart_rate as numeric)), 2) as average_heart_rate_by_gender,
ROUND(AVG(CAST(body_temp as numeric)), 2) as average_body_temp_by_gender
FROM calories
GROUP BY gender
