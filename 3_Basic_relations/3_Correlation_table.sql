SELECT 'duration', 'heart rate', ROUND(CORR(duration, heart_rate)::numeric,3) as correlation  FROM calories
UNION ALL
SELECT 'duration', 'body temp', ROUND(CORR(duration, body_temp)::numeric,3) FROM calories
UNION ALL
SELECT 'duration', 'calories', ROUND(CORR(duration, calories)::numeric,3) FROM calories
UNION ALL
SELECT 'heart rate', 'body temp', ROUND(CORR(heart_rate, body_temp)::numeric,3) FROM calories
UNION ALL
SELECT 'heart rate', 'calories', ROUND(CORR(heart_rate, calories)::numeric,3) FROM calories
UNION ALL
SELECT 'body temp', 'calories', ROUND(CORR(body_temp, calories)::numeric,3) FROM calories
