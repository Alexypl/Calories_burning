SELECT ROUND(CORR(duration, calories)::numeric, 3) as duration_vs_calories,
ROUND(CORR(heart_rate, calories)::numeric, 3) as heartrate_vs_calories,
ROUND(CORR(body_temp, calories)::numeric, 3) as bodytemp_vs_calories
FROM calories
