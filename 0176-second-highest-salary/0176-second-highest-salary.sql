# Write your MySQL query statement below

select 
    max(salary) as SecondHighestSalary -- !) 아래 주석 참고
from (
select 
    id
    , salary
    , dense_rank() over(order by salary desc) as r
from Employee
) base
where r = 2
limit 1

/*
IFNULL(val, null)은 값이 비어 있으면 'null'을 반환하지 않는다.
(IFNULL은 비어 있는 값을 원하는 값으로 가정한다.) 
이 문제를 방지하려면 MAX() 또는 하위 쿼리(IFNULL((subquery), null)를 사용해야 한다.
*/

# 예제 1
/*
SELECT max(Salary)
FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)
*/

# 예제 2
/*
SELECT DISTINCT salary
  FROM Employee a
 WHERE 2> (SELECT COUNT(DISTINCT salary) FROM Employee b WHERE b.salary > a.salary )
 ORDER BY 1 DESC
 LIMIT 2 OFFSET 1
*/

-- 참고) https://leetcode.com/problems/second-highest-salary/discuss/1168444/Summary-Five-ways-to-solve-the-top-n-nth-problems