# Write your MySQL query statement below

/*
select p.product_id, ROUND((SUM(units * price) / SUM(units)), 2) as average_price
from Prices p
inner join UnitsSold u
on p.product_id = u.product_id
and p.start_date <= u.purchase_date
and u.purchase_date <= p.end_date
group by p.product_id
*/

-- 예제 1
SELECT a.product_id,ROUND(SUM(b.units*a.price)/SUM(b.units),2) as average_price
FROM Prices as a
JOIN UnitsSold as b
ON a.product_id=b.product_id AND (b.purchase_date BETWEEN a.start_date AND a.end_date)
GROUP BY product_id;

