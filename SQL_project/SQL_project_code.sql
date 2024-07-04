/* This is a file demonstrating the SQL query skills
	
   The database consists of the following table:
   customers
   orders
   order_items
   order_payment
   products

   There are 8 sets of query with different purposes in total in this file*/


/*query set to check the existence of the table "customers" */

IF EXISTS(
SELECT
	*
	FROM
	INFORMATION_SCHEMA.TABLES 
	WHERE TABLE_NAME='customers')
	SELECT 'found' AS result ELSE SELECT' not found' AS result;


/*query to update a new record in the customers table*/

INSERT INTO customers (["customer_id"],["customer_unique_id"],["customer_zip_code_prefix"],["customer_city"],["customer_state"])

VALUES ('88rrjf88899', 'j99fjfif09', '4000', 'Hong Kong','SP');


/*query to delect a specific record in the customer table*/

DELETE FROM customers WHERE customers.["customer_id"]='88rrjf88899'


/* query set to show the number of order count corresponding to the order state*/

SELECT 
	COUNT(orders.["order_id"]) no_of_order,
	orders.["order_status"]

	FROM [sql_project].[dbo].[orders] orders

	GROUP BY orders.["order_status"]
	;


/* query set to show the total weight of the goods need to be handled before "10/7/2018  12:30:45" */

SELECT 
	SUM(products.["product_photos_qty"] *products.["product_weight_g"]) sum_of_weight

	FROM [sql_project].[dbo].[products] products, [sql_project].[dbo].[order_items] order_items

	WHERE products.["product_id"]= order_items.["product_id"] AND order_items.["shipping_limit_date"] < '10/7/2018  12:30:45'
	;

/* query set to show all the city having more than 400 customers in descending order */

SELECT
	customers.["customer_city"],
	COUNT(customers.["customer_unique_id"]) no_of_customers

	FROM [sql_project].[dbo].[customers] customers

	GROUP BY customers.["customer_city"]

	HAVING  COUNT(customers.["customer_unique_id"])>400

	ORDER BY COUNT(customers.["customer_unique_id"]) DESC
	;


/*query set to show all the customer id that the customer order a product with area greater than 50 in ascending order */

SELECT

	customers.["customer_id"],
	products.["product_length_cm"]*products.["product_width_cm"] area

	FROM [sql_project].[dbo].[orders] orders,[sql_project].[dbo].[customers] customers, [sql_project].[dbo].[order_items] order_items, [sql_project].[dbo].[products] products
 
	WHERE customers.["customer_id"] = orders.["customer_id"] AND order_items.["order_id"] = orders.["order_id"] AND order_items.["product_id"]= products.["product_id"]
	AND products.["product_length_cm"]*products.["product_width_cm"] >50

	ORDER BY area ASC
    ;


/* query set to show all the customer id that the customer use credit card to pay the bill */

SELECT
	customers.["customer_id"],
	order_payment.["payment_type"]
    
	FROM [sql_project].[dbo].[orders] orders,[sql_project].[dbo].[customers] customers, [sql_project].[dbo].[order_payments] order_payment
  
	WHERE customers.["customer_id"] = orders.["customer_id"] AND order_payment.["order_id"] = orders.["order_id"] AND order_payment.["payment_type"] = 'credit_card'
    ;


