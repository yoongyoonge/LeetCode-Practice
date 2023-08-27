# Write your MySQL query statement below


/* -- 하루에 최소 한 주문이 들어온다고 했는데 테스트 케이스 중에 그러지 못한 샘플이 있음
select 
step2.visited_on
, step2.amount
, step2.average_amount
from (
    select 
    visited_on
    , SUM(amt) over(ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as amount 
    , ROUND(AVG(amt) over(ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) as average_amount 
    from (
        select
            visited_on
            , sum(amount) as amt
        from Customer 
        group by visited_on
    ) step1
    group by visited_on
) step2
where DATE_SUB(step2.visited_on, INTERVAL 6 DAY) >= (select min(visited_on) from Customer)
order by step2.visited_on
*/

# 예제1 -- 이 코드도 테스트케이스를 모두 통과하지는 않음
/*
SELECT a.visited_on AS visited_on, SUM(b.day_sum) AS amount,
       ROUND(AVG(b.day_sum), 2) AS average_amount
FROM
  (SELECT visited_on, SUM(amount) AS day_sum FROM Customer GROUP BY visited_on ) a,
  (SELECT visited_on, SUM(amount) AS day_sum FROM Customer GROUP BY visited_on ) b
WHERE DATEDIFF(a.visited_on, b.visited_on) BETWEEN 0 AND 6
GROUP BY a.visited_on
HAVING COUNT(b.visited_on) = 7
*/

# 예제2
/*
SELECT   visited_on, 
         SUM(SUM(amount)) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)   AS'amount',
         ROUND(CAST(SUM(SUM(amount)) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS FLOAT)/7.0 ,2) AS'average_amount' 
FROM     Customer 
GROUP BY visited_on
ORDER BY visited_on
OFFSET 6 ROWS  -- Mysql server sql
*/

# 예제 3 -- 이 코드 참고 필요
WITH day AS(
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on)

SELECT d1.visited_on, SUM(d2.amount) as amount, ROUND(SUM(d2.amount)/7,2) as average_amount
FROM day d1
JOIN day d2
ON  DATEDIFF(d1.visited_on,d2.visited_on) <= 6 AND DATEDIFF(d1.visited_on,d2.visited_on) >= 0
WHERE d1.visited_on  >= (SELECT MIN(visited_on) FROM day) + 6
GROUP BY d1.visited_on
ORDER BY d1.visited_on