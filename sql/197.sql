# Write your MySQL query statement below
SELECT id
FROM(
    SELECT id, recordDate, temperature,
            LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
            LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date
    FROM Weather
    ORDER BY recordDate
    ) t
WHERE temperature > prev_temp
        AND DATEDIFF(recordDate, prev_date) = 1
;