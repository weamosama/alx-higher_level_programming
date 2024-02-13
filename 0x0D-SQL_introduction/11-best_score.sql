-- 11. Best scores in second_table
-- This script lists all records with a score >= 10 in the table second_table
-- in the database hbtn_0c_0, displaying both the score and the name, ordered by score (top first)

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
