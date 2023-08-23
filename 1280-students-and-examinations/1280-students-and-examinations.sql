# Write your MySQL query statement below
select 
    s.student_id
    , s.student_name
    , sj.subject_name 
    , count(e.cnt) as attended_exams
from Students s
inner join Subjects sj
left outer join (select student_id, subject_name, 1 as cnt from Examinations) e
on s.student_id = e.student_id
and sj.subject_name = e.subject_name
group by s.student_id, s.student_name, sj.subject_name
order by s.student_id, sj.subject_name 