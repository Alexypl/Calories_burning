SELECT MIN(height) as min_height,
percentile_disc(0.25) WITHIN GROUP (ORDER BY height) as height_1_queartile,
percentile_disc(0.5) WITHIN GROUP (ORDER BY height) as height_median,
percentile_disc(0.75) WITHIN GROUP (ORDER BY height) as height_3_queartile,
MAX(height) as max_height
FROM calories
