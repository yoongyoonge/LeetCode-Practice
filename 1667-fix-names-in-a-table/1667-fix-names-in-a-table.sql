# Write your MySQL query statement below
select 
    user_id
    , CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) as name
from Users 
order by user_id asc


# 예제 1
/*
SELECT user_id, CONCAT(UPPER(LEFT(name,1)),LOWER(RIGHT(name,LENGTH(name)-1))) AS name
FROM Users
ORDER BY user_id ASC;
*/