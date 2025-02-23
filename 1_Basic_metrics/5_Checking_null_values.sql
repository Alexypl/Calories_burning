SELECT
COUNT(*) - COUNT(User_ID),
COUNT(*) - COUNT(Gender),
COUNT(*) - COUNT(Age),
COUNT(*) - COUNT(Height),
COUNT(*) - COUNT(Weight),
COUNT(*) - COUNT(Duration),
COUNT(*) - COUNT(Heart_Rate),
COUNT(*) - COUNT(Body_Temp),
COUNT(*) - COUNT(Calories) 
FROM calories
