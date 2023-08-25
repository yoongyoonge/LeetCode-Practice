# Write your MySQL query statement below
select distinct     
    employee_id
    , department_id 
from (
    select 
        employee_id
        , department_id 
    from Employee e1
    group by employee_id
    having count(*) = 1
    union all
    select 
        employee_id
        , department_id
    from Employee e2
    where primary_flag = "Y"
) base