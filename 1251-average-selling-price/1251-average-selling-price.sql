# Write your MySQL query statement below

select p.product_id, ROUND((SUM(units * price) / SUM(units)), 2) as average_price
from Prices p
inner join UnitsSold u
on p.product_id = u.product_id
and p.start_date <= u.purchase_date
and u.purchase_date <= p.end_date
group by p.product_id
