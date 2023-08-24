# Write your MySQL query statement below


select 
    round(count(case when DATEDIFF(base.lead_event_date, base.event_date) = 1 then 1 end) / count(distinct player_id), 2) as fraction
from (
    select 
        player_id
        , event_date
        , LEAD(event_date) OVER (partition by player_id order by event_date asc) as lead_event_date
        , min(event_date) OVER (partition by player_id order by event_date asc) as min_event_date
    from Activity a
) base
where event_date = min_event_date

