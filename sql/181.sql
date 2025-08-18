# Write your MySQL query statement below
SELECT workers.name AS Employee
FROM
    (
    SELECT id, name, salary, managerId
    FROM Employee
    ) workers
INNER JOIN
    (
    SELECT id, name, salary
    FROM Employee
    ) boss
ON workers.managerId = boss.id
WHERE workers.salary > boss.salary
;