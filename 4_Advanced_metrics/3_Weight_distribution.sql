SELECT MIN(weight) as min_weight,
percentile_disc(0.25) WITHIN GROUP (ORDER BY weight) as weight_1_queartile,
percentile_disc(0.5) WITHIN GROUP (ORDER BY weight) as weight_median,
percentile_disc(0.75) WITHIN GROUP (ORDER BY weight) as weight_3_queartile,
MAX(weight) as max_weight
FROM calories
