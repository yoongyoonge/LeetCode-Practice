# Write your MySQL query statement below


select 
    i.id
    , s.student
from (
    select
        a.id
        , coalesce((case when (a.id%2)=0 then a.pre_id
               else a.next_id end), a.id) as switch_id
    from (
        select
            id
            , lag(id) over(order by id asc) as pre_id
            , lead(id) over(order by id asc) as next_id
        from Seat
    ) a
) i
inner join (
    select id, student 
    from Seat
) s
on i.switch_id = s.id
order by i.id

# 예제 1
/* -- id 를 조작
SELECT
	CASE
		WHEN seat.id % 2 <> 0 AND seat.id = (SELECT COUNT(*) FROM seat) THEN seat.id
		WHEN seat.id % 2 = 0 THEN seat.id - 1
		ELSE
			seat.id + 1
	END as id,
	student 
FROM seat
ORDER BY id
;
*/

# 예제 2
/*
SELECT ROW_NUMBER() OVER() id, student
FROM seat
ORDER BY IF(MOD(id, 2) = 0, id-1, id+1)
*/