# Write your MySQL query statement below
select v.customer_id, count(v.visit_id) as count_no_trans
from Visits v
left outer join (select distinct visit_id from Transactions) t
on v.visit_id = t.visit_id
where t.visit_id is null
group by customer_id