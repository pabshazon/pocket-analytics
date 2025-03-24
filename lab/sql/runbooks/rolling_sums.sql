-- Rolling Sums and Averages:
-- Question: Calculate the 7-day rolling average of sales.

with total_sales_per_day as (
  select
    OrderDate::date AS SaleDate,
    sum(totaldue) as total_day_sales
  from sales.SalesOrderHeader
  GROUP BY OrderDate::date
  ORDER BY OrderDate::date
)

select
	SaleDate,
  total_day_sales,
  sum(total_day_sales) OVER (ORDER BY SaleDate ROWS BETWEEN 7 PRECEDING AND CURRENT ROW) as rollingsum,
  avg(total_day_sales) OVER (ORDER BY SaleDate ROWS BETWEEN 7 PRECEDING AND CURRENT ROW) as rollingavg
from total_sales_per_day;

