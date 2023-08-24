# Write your MySQL query statement below
select 
    r.contest_id
    , round((r.parti / u.user_cnt)*100, 2) as percentage
from (
    select 
        contest_id
        , count(user_id) as parti
    from Register 
    group by contest_id
) r
inner join (
    select count(user_id) as user_cnt
    from Users
) u
order by percentage desc, contest_id asc