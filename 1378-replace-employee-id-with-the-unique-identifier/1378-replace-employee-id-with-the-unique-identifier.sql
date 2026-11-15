# Write your MySQL query statement below
SELECT u.unique_id, s.name
FROM Employees as s 
LEFT JOIN EmployeeUNI as u
ON s.id = u.id;