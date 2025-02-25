SELECT ROUND(CORR(age, calories)::numeric, 3) as age_vs_calories,
ROUND(CORR(height, calories)::numeric, 3) as height_vs_calories,
ROUND(CORR(weight, calories)::numeric, 3) as height_vs_calories
FROM calories
