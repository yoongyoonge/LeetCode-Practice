# Write your MySQL query statement below
select project_id, ROUND(SUM(experience_years)/COUNT(p.employee_id), 2) as average_years
from Project p
inner join Employee e
on p.employee_id = e.employee_id
group by project_id