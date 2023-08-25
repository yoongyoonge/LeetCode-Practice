# Write your MySQL query statement below
select 
    activity_date as day
    , count(distinct user_id) active_users 
from Activity a
where DATE_SUB('2019-07-27', INTERVAL 30 DAY) < activity_date
and activity_date < '2019-07-27'
-- where datediff('2019-07-27', activity_date) <30 -- 이렇게도 조건을 쓸 수 있다 
-- 물론 between으로도 그냥 수동 계산해서 넣을수도있다.
-- 문제 조건 잘못이해: '2019-07-27' 이전 30일 이내의 유저 수를 계산해야함
group by activity_date

