# Write your MySQL query statement below
select
    query_name
    , round(SUM(rating/position)/COUNT(query_name), 2) as quality
    , round(SUM(case when rating < 3 then 1 else 0 end)/COUNT(query_name)*100, 2) as poor_query_percentage
from Queries
group by query_name
-- sum 이라서 else 0 써야하는데 까먹어서 뒤늦게 추가