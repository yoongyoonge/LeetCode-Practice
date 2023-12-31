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
-- 예제의 런타임이 더 성능이 좋은 줄 알았는데 아님... 그냥 다른 풀이라고 생각
-- 다른점은 on 조건에서 between을 사용한 것
