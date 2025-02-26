SELECT MIN(age) as min_age,
percentile_disc(0.25) WITHIN GROUP (ORDER BY age) as age_1_queartile,
percentile_disc(0.5) WITHIN GROUP (ORDER BY age) as age_median,
percentile_disc(0.75) WITHIN GROUP (ORDER BY age) as age_3_queartile,
MAX(age) as max_age
FROM calories
