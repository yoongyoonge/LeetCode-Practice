# Write your MySQL query statement below

select 
    product_name
    , sum_unit as unit
from (
    select 
        product_id
        , sum(unit) as sum_unit
    from Orders
    where order_date like '2020-02%'
    group by product_id
    having sum(unit) >= 100
) o
inner join (
    select 
        product_id
        , product_name
    from Products 
) p
on o.product_id = p.product_id