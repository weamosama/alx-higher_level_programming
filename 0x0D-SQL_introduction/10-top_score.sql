-- 10. Top scores in second_table
-- This script lists all records of the table second_table in the database hbtn_0c_0
-- displaying both the score and the name, ordered by score (top first)

SELECT score, name FROM second_table ORDER BY score DESC;
