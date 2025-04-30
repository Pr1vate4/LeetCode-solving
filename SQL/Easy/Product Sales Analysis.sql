--простая задачка, чисто освежить базу
SELECT product_name, year, price
from Sales
JOIN Product ON Sales.product_id = Product.product_id