# Write your MySQL query statement below

select 
    product_id
    , new_price as price
from (
select 
    product_id 
    , new_price 
    , change_date
    , max(change_date) over(partition by product_id) as max_date
from Products p
where change_date <= "2019-08-16"
) a
where change_date = max_date
union all
select distinct
    product_id 
    , 10 as new_price
from Products p
where change_date > "2019-08-16"
and product_id not in (select distinct product_id from Products where change_date <= "2019-08-16")