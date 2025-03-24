-- Question: Find the top 3 products by sales amount.​
WITH orders_with_lines_totaled as (
  SELECT
      productid,
      sum(orderqty * unitprice) as linetotal
  FROM sales.SalesOrderDetail
  GROUP BY productid
  ORDER BY linetotal desc
)

SELECT
	productid,
  linetotal,
  DENSE_RANK() OVER (ORDER BY linetotal DESC) AS rank
FROM orders_with_lines_totaled;

