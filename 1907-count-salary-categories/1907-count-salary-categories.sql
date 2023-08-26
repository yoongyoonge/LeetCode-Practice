# Write your MySQL query statement below



select catg.category
, coalesce(cnt.accounts_count, 0) as accounts_count
from (
    select 'Low Salary' as category
    union 
    select 'Average Salary' as category
    union 
    select 'High Salary' as category
) catg
left outer join (
    select category
    , count(*) as accounts_count
    from (
    select 
        account_id 
        , case when income < 20000 then "Low Salary" 
               when income > 50000 then "High Salary" 
               else "Average Salary" end as category
    from Accounts
    ) base
    group by category
) cnt
on catg.category = cnt.category