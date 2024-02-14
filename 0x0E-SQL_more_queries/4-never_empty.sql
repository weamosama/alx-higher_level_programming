-- 4-never_empty.sql

-- Create or update the table 'id_not_null' if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1 NOT NULL,
    name VARCHAR(256)
);
