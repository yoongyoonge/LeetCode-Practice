# Write your MySQL query statement below

# 예제 1
select * from Users 
where regexp_like(mail, '^[A-Za-z]+[A-Za-z0-9\_\.\-]*@leetcode\\.com')

-- 참고)https://leetcode.com/problems/find-users-with-valid-e-mails/discuss/746476/A-character-by-character-explanation-of-regular-expression