-- This script lists the privileges of MySQL users user_0d_1 and user_0d_2 on localhost;
SELECT
    grantee,
    privilege_type,
    is_grantable
FROM
    information_schema.user_privileges
WHERE
    grantee = 'user_0d_1@localhost' OR grantee = 'user_0d_2@localhost';
