# Write your MySQL query statement below
select 
    s.product_id 
    , s.year as first_year
    , s.quantity 
    , s.price 
from Sales s
inner join (
    select 
        product_id
        , min(year) as min_year
    from Sales
    group by product_id 
) min_base
on s.product_id = min_base.product_id
and s.year = min_base.min_year

/* -- 다른 버전
SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (
SELECT product_id, MIN(year) as year
FROM Sales
GROUP BY product_id) ;
*/