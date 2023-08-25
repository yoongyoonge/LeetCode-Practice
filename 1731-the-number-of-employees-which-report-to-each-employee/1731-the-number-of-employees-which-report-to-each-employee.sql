# Write your MySQL query statement below

select 
    employee_id 
    , name 
    , reports_count
    , average_age
from (
    select 
        employee_id 
        , name 
    from Employees e
    where employee_id in (
        select distinct reports_to 
        from Employees e
        where reports_to is not null
    )
) base 
inner join (
    select 
        reports_to 
        , count(*) as reports_count 
        , round(AVG(age), 0) as average_age 
    from Employees e
    where reports_to is not null
    group by reports_to
) cal
on base.employee_id = cal.reports_to
order by employee_id