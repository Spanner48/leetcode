SELECT category_list.category, COALESCE(accounts_count, 0) AS accounts_count
FROM (
    SELECT 'Low Salary' AS category
    UNION
    SELECT 'Average Salary'
    UNION
    SELECT 'High Salary'
) AS category_list
LEFT JOIN (
    SELECT category, COUNT(category) AS accounts_count
    FROM (
        SELECT account_id, income,
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income <= 50000 THEN 'Average Salary'
            WHEN income > 50000 THEN 'High Salary'
            ELSE '0' END AS category
        FROM Accounts) a1
    GROUP BY category) AS counts
    ON category_list.category = counts.category;
;