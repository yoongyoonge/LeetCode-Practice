# Write your MySQL query statement below

# user

select results
    from (
    select 
        name as results
        , row_number() over(order by rate_cnt desc, name asc) as rn
    from (
        select 
            user_id
            , count(*) as rate_cnt
        from MovieRating
        group by user_id
    ) mr
    inner join (
        select user_id, name         
        from Users 
    ) u on mr.user_id = u.user_id
) a
where rn = 1
union all
select results
from (
    select 
        title as results
        , row_number() over(order by rate_avg desc, title asc) as rn
    from (
        select 
            movie_id
            , avg(rating) as rate_avg -- 문제 조건 놓침
        from MovieRating
        where created_at like "2020-02%"
        group by movie_id
    ) mr
    inner join (
        select movie_id, title 
        from Movies
    ) m on mr.movie_id = m.movie_id 
) b
where rn = 1
