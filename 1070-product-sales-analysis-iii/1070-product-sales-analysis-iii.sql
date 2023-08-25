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