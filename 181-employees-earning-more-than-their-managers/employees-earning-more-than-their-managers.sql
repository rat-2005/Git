# Write your MySQL query statement below
Select a.name as Employee from Employee as a, Employee as b where a.salary>b.salary and b.id=a.managerId 
