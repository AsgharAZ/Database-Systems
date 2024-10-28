-- 1. Find the employee who processed the first order placed in the year 1998.
-- Output: EmployeeID
-- Result contains 10 rows

SELECT Top 1 EmployeeID
FROM Orders
WHERE OrderDate = (
    SELECT MIN(OrderDate)
    FROM Orders
    WHERE YEAR(OrderDate) = 1998
);

-- 2. Select all employees who work directly under the top manager of the company.
-- Output: EmployeeID
-- Result contains 5 rows

select Employees.EmployeeID
from Employees
where ReportsTo = (
	select Employees.EmployeeID
	from Employees
	where ReportsTo is null
);


-- 3. Select all employees who are assigned to territories in the 'Western' and 'Eastern' regions from the Region Table.
-- Output: EmployeeID
-- Result contains 6 rows

select distinct EmployeeTerritories.EmployeeID
from EmployeeTerritories
where EmployeeTerritories.TerritoryID IN (
	select Territories.TerritoryID
	from Territories
	where Territories.RegionID IN (
		select RegionID 
		from Region
		where RegionDescription = 'Western' or RegionDescription = 'Eastern'
	)
);

-- 4. Select all Customers and Suppliers belonging to ‘Germany’.
-- Output: ContactName
-- Result contains 14 rows

select ContactName 
from Customers
where Country = 'Germany'

Union 

select ContactName 
from Suppliers
where Country = 'Germany'


-- 5. Find the 3rd most expensive product in the database.
-- Output: ProductName
-- Result contains 1 row

select Top 1 ProductName
from (
	select Top 3 *
	from Products
	order by UnitPrice DESC
	) as subtable
order by UnitPrice ASC;

-- 6. Select all employees and their Seniority level:
-- • Seniority level = 3 if employee has been with the company for more than 5 years.
-- • Seniority level = 2 if employee has been with the company from 3-5 years.
-- • Seniority level = 1 if employee has been with the company for less than 3 years.
-- Output: EmployeeID, SeniorityLevel
-- Result contains 9 rows

select EmployeeID,
    CASE 
        when DATEDIFF(YEAR, HireDate, GETDATE()) > 5 then 3
        when DATEDIFF(YEAR, HireDate, GETDATE()) BETWEEN 3 AND 5 then 2
        else 1
    END 
	AS SeniorityLevel
from Employees;


-- 7. List all products and their types which indicate if they are:
-- • Costly (unit price > 80)
-- • Economical (unit price between 30 and 80)
-- • Cheap (unit price < 30)
-- Output: ProductName, Types
-- Result contains 77 rows

select Products.ProductName,
    CASE 
        when UnitPrice > 80 then 'costly'
        when UnitPrice BETWEEN 30 AND 80 then 'Economical'
		when UnitPrice < 30 then 'Cheap'
    END 
	AS Types
from Products;



-- 8. List all products and their trends based on the number of orders placed in the year 1997.
-- • Trend = Customer favourite if no. of orders >= 50
-- • Trend = Trending if 30 <= no. of orders <= 49
-- • Trend = On the rise if 10 <= no. of orders <= 29
-- • Trend = Not popular if no. of orders < 10
-- Output: ProductName, Trend
-- Result contains 77 rows

select ProductName,
    CASE 
        when TotalProductsSold >= 50 then 'Customer Favourite'
        when TotalProductsSold BETWEEN 30 AND 49 then 'Trending'
		when TotalProductsSold BETWEEN 10 AND 29 then 'On the rise'
		when TotalProductsSold < 10 then 'Not Popular'
    END 
	AS Trend
from (
	select Products.ProductName, [Order Details].ProductID, sum(Quantity) as TotalProductsSold
	from [Order Details]
	inner join Products on Products.ProductID = [Order Details].ProductID
	where OrderID in (
		select OrderID
		from Orders
		where YEAR(OrderDate) = '1997')
	group by [Order Details].ProductID, Products.ProductName
	--order by TotalProductsSold DESC
	) as subtable

-- 9. Find the total number of orders placed by each customer.
-- Output: CustomerID
-- Result contains 91 rows

select Customers.CustomerID, count(Orders.OrderID) as [Order Count]
from Orders
Right join Customers on Orders.CustomerID = Customers.CustomerID
group by Customers.CustomerID
order by [Order Count] DESC


-- 10. Retrieve customers who have placed orders for products with a price higher than the average price of all products.
-- Output: CustomerID
-- Result contains 86 rows

select distinct CustomerID
from Orders
where OrderID in (
	select OrderID
	from [Order Details]
	where UnitPrice > (
						select avg(UnitPrice)
						from Products
						)
)

-- 11. Find the customers who have placed orders for products from the same category as ‘Chai’.
-- Output: Customers.ContactName
-- Result contains 83 rows

select Customers.ContactName
from Customers
where Customers.CustomerID in (
    select Orders.CustomerID
    from Orders
    where Orders.OrderID in (
        select OrderDetails.OrderID
        from [Order Details] OrderDetails
        where OrderDetails.ProductID in (
            select Products.ProductID
            from Products
            where Products.CategoryID in (
                select Products.CategoryID
                from Products
                where Products.ProductName = 'Chai'
            )
        )
    )
)
order by Customers.ContactName;



-- 12. Find the customer who has placed the highest total number of orders.
-- Output: ContactName, NumberOfOrders
-- Result contains 1 row

select ContactName, NumberOfOrders
from Customers
Right join
	(
	select Top 1 CustomerID, Count(Orders.OrderID) as 'NumberOfOrders'
	from Orders
	group by Orders.CustomerID
	Order By 'NumberOfOrders' Desc
	) A on A.CustomerID = Customers.CustomerID


-- 13. List all the customers who have placed an order for the most expensive product.
-- Output: ContactName
-- Result contains 12 rows
Select ContactName
From Customers
where CustomerID in
	(Select CustomerID
	from Orders 
	where OrderID in 
		(Select OrderID
		from [Order Details]
		where [Order Details].UnitPrice = 	
			(Select Max(UnitPrice)
			from Products)))

-- 14. Find the average number of products in each order.
-- Output: AverageProductsPerOrder
-- Result contains 1 row

select avg(avgQuantityPerOrder) as AverageProductsPerOrder
from (select count(Quantity) as avgQuantityPerOrder
	from [Order Details]
	group by OrderID) as subtable

-- 15. Find the categories where the average product price is higher than the overall average product price.
-- Output: CategoryName
-- Result contains 3 rows
select CategoryName
from Categories
where CategoryID in (
    select CategoryID
    from Products
    group by CategoryID
    having AVG(UnitPrice) > (select AVG(UnitPrice) from Products)
)

-- 16. Find the product which has the second highest price.
-- Output: ProductName, UnitPrice

-- Result contains 1 row
select Top 1 ProductName
from (
	select Top 2 *
	from Products
	order by UnitPrice DESC
	) as subtable
order by UnitPrice ASC;


-- 17. Find the average order amount for customers from France.
-- Output: AverageOrderAmount
-- Result contains 1 row

select (
    select avg(TotalAmount)
    from (
        select sum(OrderDetails.UnitPrice * OrderDetails.Quantity) as TotalAmount
        from Orders
        inner join [Order Details] OrderDetails on Orders.OrderID = OrderDetails.OrderID
        where Orders.CustomerID in (
            select Customers.CustomerID
            from Customers
            where Customers.Country = 'France'
        )
        group by Orders.OrderID
    ) as OrderTotals
) as AverageOrderAmount;