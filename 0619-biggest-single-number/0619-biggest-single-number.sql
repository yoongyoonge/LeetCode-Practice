# Write your MySQL query statement below

select max(num) as num
from MyNumbers
where num in (
    select num
    from MyNumbers m
    group by num
    having count(*) = 1
)

/* -- 이런 풀이도 있다
select(
  select num
  from number
  group by num
  having count(*) = 1
  order by num desc limit 1
) as num;
*/