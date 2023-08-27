# Write your MySQL query statement below

select 
    dp.name as Department
    , base.name as Employee 
    , salary
from (
    select
        departmentId
        , name
        , salary
        , dense_rank() over(partition by departmentId order by salary desc) as r
    from Employee e
) base
inner join (select id, name from Department) dp
on base.departmentId = dp.id
where r <= 3
