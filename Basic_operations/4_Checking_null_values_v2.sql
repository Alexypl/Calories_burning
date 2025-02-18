SELECT column_name, 
       COUNT(*) - COUNT(*) FILTER (WHERE column_name IS NOT NULL) AS null_count
FROM information_schema.columns
CROSS JOIN calories
WHERE table_name = 'calories'
GROUP BY column_name;
