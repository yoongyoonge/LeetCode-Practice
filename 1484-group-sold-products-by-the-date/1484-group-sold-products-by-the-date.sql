# Write your MySQL query statement below


select 
    sell_date
    , count(*) as num_sold
    , group_concat(product order by product asc separator ',') as products -- group_concat을 처음 알게 되었다!
from (
    select distinct sell_date, product
    from Activities a
) base
group by sell_date
order by sell_date asc
