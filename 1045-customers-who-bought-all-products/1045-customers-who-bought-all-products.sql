# Write your MySQL query statement below

select customer_id 
from (
    select customer_id, count(distinct product_key) as buy_prd_cnt
    from Customer 
    group by customer_id
) c
where buy_prd_cnt = (
    select count(distinct product_key)
    from Product p
)


