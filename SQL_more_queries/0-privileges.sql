-- This script lists the privileges of MySQL users user_0d_1 and user_0d_2 on localhost.

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Show privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Grant specific privileges to user_0d_2
GRANT SELECT, INSERT, UPDATE, DELETE ON database.* TO 'user_0d_2'@'localhost';

-- Show privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
