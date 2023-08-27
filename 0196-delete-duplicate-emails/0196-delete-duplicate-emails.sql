# Write your MySQL query statement below


delete from Person where id not in (
select 
    min_id
from (
    select email
    , min(id) as min_id
    from Person
    group by email
    ) step1
)

# 예제 1
/*
delete p1 from person p1,person p2 
where p1.email=p2.email and p1.id>p2.id;
*/
