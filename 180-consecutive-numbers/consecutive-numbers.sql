# Write your MySQL query statement below
SELECT DISTINCT(num) as ConsecutiveNums  FROM
(SELECT num,LEAD(num,1) OVER(ORDER BY id) as num2,LEAD(num,2) OVER(ORDER BY id) as num3 from LOGS) as q
WHERE num=num2 AND num=num3
