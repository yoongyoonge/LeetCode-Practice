# Write your MySQL query statement below

select
     person_name
from Queue q
where turn = (
    select 
         max(turn) as max_turn
    from (
         select 
             turn
             , person_id  
             , person_name 
             , weight
             , (sum(weight) over (order by turn asc)) - 1000 as total_weight
         from Queue q
         order by turn
    ) base
    where base.total_weight <= 0
)
