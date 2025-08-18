# Write your MySQL query statement below
SELECT dept AS Department, name AS Employee, salary AS Salary
FROM(
    SELECT e.id, e.name, e.salary, d.name AS dept,
        RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS rnk
    FROM Employee e
    LEFT JOIN
    Department d
    ON e.departmentId = d.id
    ) t
WHERE rnk = 1
;