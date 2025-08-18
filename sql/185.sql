SELECT d.name as Department, e.name as Employee, Salary
FROM Employee e, Department d
WHERE e.departmentId = d.id AND (
    SELECT Count(DISTINCT e2.Salary)
    FROM Employee e2
    WHERE e2.Salary > e.Salary AND
    e.departmentId = e2.departmentId
) < 3
;