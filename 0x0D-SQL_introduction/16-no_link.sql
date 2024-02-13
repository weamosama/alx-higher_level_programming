-- 16. No link
-- This script lists all records of the table second_table in the database hbtn_0c_0
-- excluding rows without a name value, displaying the score and the name,
-- listed by descending score


SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
