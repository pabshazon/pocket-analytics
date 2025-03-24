-- Question: Create a table that shows the cumulative sales amount for each day, including previous days`

WITH DailySales AS (
    SELECT
        OrderDate::date AS SaleDate,
        SUM(totaldue) AS TotalSales
    FROM sales.SalesOrderHeader
    GROUP BY SaleDate
)
SELECT
    SaleDate,
    TotalSales,
    SUM(TotalSales) OVER (ORDER BY SaleDate ORDER BY SaleDate) AS CumulativeSales
FROM DailySales;


