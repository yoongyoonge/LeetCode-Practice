# Write your MySQL query statement below

select 
    round(count(case when order_date = customer_pref_delivery_date then 1 end) / count(*) * 100, 2) as immediate_percentage
from Delivery d
inner join (
    select 
        customer_id
        , min(order_date) as min_order_date
    from delivery
    group by customer_id
) min_base
on d.customer_id = min_base.customer_id
where d.order_date = min_base.min_order_date
