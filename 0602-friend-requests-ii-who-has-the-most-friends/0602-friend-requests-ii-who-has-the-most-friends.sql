# Write your MySQL query statement below



select 
    id
    , sum(cnt) as num
from (
    select 
        accepter_id as id
        , count(*) as cnt
    from RequestAccepted ra
    group by accepter_id
    union all
    select
        requester_id as id
        , count(*) as cnt
    from RequestAccepted ra
    group by requester_id
) base
group by id
order by num desc
limit 1