​- 어떤 유저가 남긴글
https://leetcode.com/problems/invalid-tweets/discuss/968440/MySQL%3A-LENGTH()-is-incorrect.-Important-difference-between-CHAR_LENGTH()-vs-LENGTH()

- length는 바이트 단위로 측정된 문자열 길이를 반환하는 거라 원래는 맞지 않는다고 한다.
- 콘텐츠에 사용된 문자 수를 정확히 세려면 CHAR_LENGTH를 써야한다고 한다.

``` sql
SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15

-- Example:

SELECT LENGTH('€')  # is equal to 3
SELECT CHAR_LENGTH('€') # is equal to 1

```
- Important Note: Using LENGTH() will pass the testcases. If the testcases included characters such as € then it would fail as shown in the examples above.
- 문제는 length 를 써도 통과하지만 특수문자가 있을 경우 결과가 달라질 수 있는 것을 알아야한다.