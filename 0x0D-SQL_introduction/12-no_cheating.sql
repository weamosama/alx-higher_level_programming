-- 12. No cheating update
-- This script updates the score of Bob to 10 in the table second_table
-- using only the name field (not using Bob’s id value)

UPDATE second_table SET score = 10 WHERE name = 'Bob';
