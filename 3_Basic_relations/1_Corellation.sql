SELECT CORR(duration, calories) as duration_vs_calories,
CORR(heart_rate, calories) as heartrate_vs_calories,
CORR(body_temp, calories) as bodytemp_vs_calories
FROM calories
