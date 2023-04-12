SET search_path = my_schema, "$user",salesordersexample ;
-- 1
-- select custfirstname, orderdate
-- from customers 
-- inner join orders  on customers.customerid = orders.customerid
-- order by orders.orderdate asc

-- 2
-- select vendname, productname 
-- from products  
-- inner join product_vendors on products.productnumber = product_vendors.productnumber
-- inner join vendors  on product_vendors.vendorid = vendors.vendorid
-- where wholesaleprice < 100

-- 3
-- select distinct custfirstname, empfirstname
-- from customers c
-- inner join orders o on c.customerid = o.customerid
-- inner join employees e
-- on o.employeeid = e.employeeid
-- where c.custlastname=e.emplastname 

-- 4
-- set search_path = my_schema, "$user", entertainmentagencyexample;
-- select agentid, entertainerid
-- from entertainers e
-- inner join agents a
-- on a.agtzipcode = e.entzipcode

-- 5
-- set search_path = my_schema, "$user", recipesexample;
-- select recipetitle from recipes r
-- where (recipeid  in
-- (select recipe_ingredients.recipeid
-- from ingredients inner join
-- recipe_ingredients on 
-- ingredients.ingredientid = recipe_ingredients.ingredientid
-- where ingredients.ingredientname = 'Beef' or
--  ingredients.ingredientname = 'Garlic'))

-- 6
-- select distinct recipetitle from recipes r
-- inner join recipe_ingredients ri
-- on r.recipeid = ri.recipeid
-- inner join ingredients i_n
-- on ri.ingredientid=i_n.ingredientid
-- where i_n.ingredientname='Milk'


-- 7
-- select distinct o.customerid
-- from orders as o
-- inner join order_details as od 
-- on od.ordernumber = o.ordernumber
-- inner join products as p 
-- on p.productnumber = od.productnumber
-- inner join categories as cp 
-- on cp.categoryid = p.categoryid
-- where cp.categorydescription = 'Bikes'
