# Write your MySQL query statement below
WITH
    t1 AS (
        SELECT player_id, event_date,
        LEAD(event_date) OVER (PARTITION BY player_id ORDER BY event_date) AS next_login
        FROM Activity
    ),
    t AS (
        SELECT
            player_id, event_date,
            MIN(event_date) AS first_login
        FROM Activity
        GROUP BY player_id
        ),
    consec AS (
        SELECT t.player_id, t.first_login, t1.next_login
        FROM t
        INNER JOIN t1
        ON t1.player_id = t.player_id
        WHERE
            next_login IS NOT NULL
            AND DATEDIFF(next_login, first_login) = 1
        ),
        cnt_consec AS (
        SELECT COUNT(DISTINCT player_id) AS x
        FROM consec
            ),
        cnt_logins AS (
            SELECT COUNT(DISTINCT player_id) AS y
            FROM t
            )
SELECT ROUND((x / y), 2) AS fraction
FROM cnt_consec
JOIN cnt_logins
;