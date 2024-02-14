-- 2-create_read_user.sql

-- Create or update the database 'hbtn_0d_2'
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create or update the user 'user_0d_2'
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant usage on all databases to 'user_0d_2'
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';

-- Grant SELECT privilege on hbtn_0d_2 database to 'user_0d_2'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;
