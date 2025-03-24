-- Question: Calculate the running total of sales for each salesperson over time.
-- select count(*) from sales.salesorderheader LIMIT 10;

-- SELECT
-- 	SalesPersonID,
--   SUM(totaldue)
-- FROM sales.salesorderheader
-- WHERE SalesPersonID = 274
-- GROUP BY SalesPersonID;
-- 1235934.4451

SELECT
	SalesPersonID,
  OrderDate,
  totaldue,
  SUM(totaldue) over (PARTITION BY SalesPersonID) as RunningTotalSales
FROM sales.salesorderheader;
--GROUP BY SalesPersonID;