# Write your MySQL query statement below
SELECT name AS Customers
FROM Customers cus
LEFT JOIN
Orders ords
ON cus.id = ords.customerId
WHERE ords.id IS NULL
;