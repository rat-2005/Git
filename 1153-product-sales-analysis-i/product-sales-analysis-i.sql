# Write your MySQL query statement below
SELECT t.product_name,s.year,s.price
FROM Sales s
JOIN Product t
ON s.product_id=t.product_id
