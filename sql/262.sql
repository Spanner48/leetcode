# Write your MySQL query statement below

SELECT request_at AS Day, ROUND(SUM(if(status LIKE 'cancelled%', 1, 0)) / COUNT(request_at), 2) AS 'Cancellation Rate'
FROM(
    SELECT request_at, status
    FROM Trips t
    INNER JOIN
        (SELECT * FROM Users WHERE banned = 'No') uc
    ON t.client_id = uc.users_id
    INNER JOIN
        (SELECT * FROM Users WHERE banned = 'No') ud
    ON t.driver_id = ud.users_id
    WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
    ) tab
GROUP BY Day
;