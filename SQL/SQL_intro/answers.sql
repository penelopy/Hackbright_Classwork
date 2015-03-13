-- Problem 1
SELECT * FROM salespeople

-- Problem 2
SELECT * FROM salespeople WHERE region = 'Northwest';

-- Problem 3
SELECT email FROM salespeople WHERE region = 'Southwest';

-- Problem 4
SELECT givenname, surname, email FROM salespeople WHERE region = 'Northwest';

-- Problem 5
SELECT common_name FROM melons WHERE price > 5;

-- Problem 6
SELECT melon_type, common_name FROM melons WHERE price >5 and melon_type = 'Watermelon';

-- Problem 7
SELECT common_name FROM melons WHERE common_name LIKE 'C%';

-- Problem 8
SELECT common_name FROM melons WHERE common_name LIKE '%Golden%';

-- Problem 9
SELECT DISTINCT(region) FROM salespeople

-- Problem 10
SELECT email FROM salespeople WHERE region = 'Northwest' or region = 'Southwest';

-- Problem 11
SELECT email FROM salespeople WHERE region IN ('Northwest', 'Southwest');

-- Problem 12
SELECT email, givenname, surname FROM salespeople WHERE region IN ('Northwest', 'Southwest') and surname LIKE 'M%';

-- Problem 13
SELECT melon_type, common_name, price AS usd, price*0.735693 AS euros FROM melons

-- Problem 14
SELECT count(*) FROM customers;

-- Problem 15
SELECT COUNT(*) FROM orders WHERE shipto_state = 'CA';

-- Problem 16
SELECT SUM(order_total) FROM orders;

-- Problem 17
SELECT AVG(order_total) FROM orders;

-- Problem 18
SELECT MIN(order_total) FROM orders;

-- Problem 19
SELECT id FROM customers WHERE email ='phyllis@demizz.edu';

-- Problem 20
SELECT id, status, order_total FROM orders WHERE customer_id = '100';

-- Problem 21
SELECT id, status, order_total FROM orders WHERE customer_id = (SELECT id FROM customers WHERE email LIKE 'phyllis@demizz.edu');

-- Problem 22
SELECT O.id, O.status, O.order_total FROM orders AS O JOIN customers as C ON C.id =  O.customer_id WHERE C.email = 'phyllis@demizz.edu';

-- Problem 23
SELECT * FROM order_items WHERE order_id = 2725;

-- Problem 24
SELECT M.common_name, M.melon_type, O.quantity, O.unit_price, O.total_price FROM melons AS M JOIN order_items AS O ON (M.id = O.melon_id) WHERE O.order_id = '2725';

-- Problem 25
SELECT SUM(O.order_total) FROM orders AS O WHERE O.salesperson_id IS NULL; 

-- Problem 26
SELECT S.givenname, S.surname, SUM(O.order_total), SUM(O.order_total)*.15 FROM salespeople AS S LEFT JOIN orders AS O ON (O.salesperson_id = S.id) GROUP BY S.id;

