# Write your MySQL query statement below
SELECT name
FROM
    (SELECT managerId, COUNT(managerId) AS cnt_reports
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING cnt_reports >= 5) e
INNER JOIN
    (SELECT id, name
    FROM Employee
    ) ee
ON e.managerId = ee.id
;