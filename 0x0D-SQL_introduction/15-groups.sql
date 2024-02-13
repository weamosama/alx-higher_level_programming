-- 15. Groups
-- This script lists the number of records with the same score in the table second_table
-- in the database hbtn_0c_0, displaying both the score and the number of records,
-- sorted by the number of records (descending)

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
