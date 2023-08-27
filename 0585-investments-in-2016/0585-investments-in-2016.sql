# Write your MySQL query statement below
select ROUND(SUM(tiv_2016), 2) as tiv_2016 
from Insurance
where pid in (
    select 
        pid
    from Insurance i
    where tiv_2015 in (
       select tiv_2015
       from Insurance 
       group by tiv_2015
       having count(*) > 1
    ) and concat(lat,lon) in (
        select concat(lat,lon) as lat_lon
        from Insurance 
        group by concat(lat,lon)
        having count(*) = 1
    )
)





