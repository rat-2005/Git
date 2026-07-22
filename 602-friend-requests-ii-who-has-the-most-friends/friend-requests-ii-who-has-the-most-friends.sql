# Write your MySQL query statement below
SELECT id,COUNT(*) as num FROM
(SELECT requester_id as id FROM RequestAccepted UNION ALL
SELECT accepter_id as id FROM RequestAccepted) as gro
GROUP BY id
ORDER by num DESC
LIMIT 1