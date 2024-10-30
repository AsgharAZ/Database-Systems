 --Insert
drop table if exists test
Create table test (testid int identity (1,1), testname
varchar (20), testdate datetime , testnumber int)
select * from test


Insert into test (testname , testdate , testnumber) values ('aaaa',getdate () ,123)
select * from test

Insert into test (testname , testdate) values ('aaaa', getdate ())
select * from test

Insert into test (testname , testdate , testnumber) values ('aaaa',(select min(orderdate) from orders) ,123)
select * from test

Select @@Identity
select scope_identity ()

Insert Into test(testname , testdate , testnumber)
Select CustomerID , OrderDate , OrderID from Orders
select * from test

-- Update
Update test
Set testName ='xyz', testnumber = 5
Where testID < 10

Update Test
Set testNumber = EmployeeID , testName = 'test'+ cast(testid as varchar (3))
From Orders
Where Orders.orderid = testNumber
select * from test


--Delete
Delete Test
Where TestID <= 10

Delete Test
Where TestNumber in (10253 ,10254)

Delete Test
Where TestNumber in (select orderid from orders where customerid = 'ALFKI ')

delete test
from employees
where testid = employeeid