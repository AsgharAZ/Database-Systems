drop table test
Create table test(testid int identity(1, 1), testname varchar(20), testdate datetime, testnumber int)
select * from test

Insert into test(testname, testdate, testnumber) values('aaaa', getdate(), 123)
Insert into test(testname, testdate) values('abcd', getdate())
Insert into test(testname, testdate, testnumber) values('pqrs', (select min(orderdate) from orders), 123)
select * from test

Select @@Identity
select scope_identity()

Update test
Set testName = 'xyz', testnumber = 5
Where testID < 10
select * from test

Update Test
Set testNumber = EmployeeID, 	
testName ='test ' + cast(testid as varchar(3))
From Orders
Where Orders.orderid = testNumber

Delete Test
Where TestID <= 10
select * from test

Delete Test
Where TestNumber in(10253, 10254)
Delete Test 
Where TestNumber in(select orderid from orders where customerid = 'ALFKI')
select * from test