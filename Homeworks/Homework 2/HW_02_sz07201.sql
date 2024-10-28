-- Syed Asghar Abbas Zaidi
-- Database Homework 2
-- Fall 2024

-- 1. List the number of employees in each department.
-- Output: Dept Name, No Of Workers.
-- Result contains 3 rows.

select DEPT_NAME, count(Dept_ID) as [No Of Workers.]
from Department
inner join worker on worker.DEPT_ID = Department.ID -- Joining Department and Worker tables to count workers by department
group by DEPT_NAME -- Group by DEPT_NAME to calculate count per department

-- 2. Display the employment history of worker 'Malik Zain'; list all his designations
-- with current designation at the top and first designation in the company at the bottom.
-- Output: First Name, Last Name, Title, Affected From.
-- Result contains 3 rows.

select FIRST_NAME, LAST_NAME, TITLE,AFFECTED_FROM
from worker
inner join title on title.WORKER_REF_ID = Worker.WORKER_ID
inner join Designation on Designation.ID = title.DESIGNATION_ID -- Join Worker, Title, and Designation tables to retrieve Malik Zain's employment history
where FIRST_NAME = 'Malik' and LAST_NAME = 'Zain'

-- 3. Display the "total salary" of all workers belonging to the department 'Admin'.
-- Output: Dept Name, Salary.
-- Result contains 1 row.

select DEPT_NAME, sum(SALARY) as SALARY
from worker
join Department on Department.ID = Worker.DEPT_ID
where DEPT_NAME = 'admin' -- Filter for the 'Admin' department
group by DEPT_NAME --  Then doing group by on the remaining rows, to calculate the total salary of the "Admin" Department.


-- 4. List all workers with their salaries and department name. If a worker has not been
-- assigned any department, show 'No Department' for those workers.
-- Output: First Name, Last Name, Salary, Dept Name.
-- Result contains 10 rows.

-- COALESCE replaces null with 'No Department'
select FIRST_NAME, LAST_NAME, SALARY, COALESCE(DEPT_NAME, 'No Department') AS [Dept Name.]
from worker
left join Department on Worker.DEPT_ID = Department.ID -- Left join to include workers with no department

-- 5. List all workers with their joining dates (without time) and total years of service.
-- Output: First Name, Last Name, Joining Date, Years.
-- Result contains 10 rows.

-- Extract year only from JOINING_DATE and calculate years of service up to the current date
select FIRST_NAME, LAST_NAME, CAST(JOINING_DATE AS DATE) as [JOINING_DATE], DATEDIFF(year, JOINING_DATE, GETDATE()) as YEARS
from Worker

-- 6. List all records of the 'Worker' entity.
-- Output: Worker ID, First Name, Last Name, Salary, Joining Date, Dept ID.
-- Result contains 10 rows.

select *
from Worker

-- 7. List all the workers who do not have any designation and are not assigned to any department.
-- Output: Worker ID, First Name, Last Name, Joining Date.
-- Result contains 2 rows.

select WORKER_ID, FIRST_NAME, LAST_NAME, JOINING_DATE
from worker
full join title on title.WORKER_REF_ID = Worker.WORKER_ID
full join Designation on Designation.ID = title.DESIGNATION_ID -- Full join with Title and Designation tables; filters for workers with no department or title
where DEPT_ID is null and DESIGNATION_ID is null -- filters for workers with no department or title

-- 8. List department names with the highest salary of the department.
-- Output: Dept Name, Salary.
-- Result contains 3 rows.

-- I am assuming here, we are being asked to list down the "highest salary" in each department
-- Technically there should exist fourth row, with department name "IT", which will have the highest salary of 0 cause there are no people there.
-- However, as the question expects "three rows", it is assumed that this side-case is intentionally meant to be neglected. 

select DEPT_NAME, max(SALARY) as SALARY
from worker
inner join Department on Department.ID = Worker.DEPT_ID
group by DEPT_NAME

-- 9. List all workers with the current designation, ordered by First Name.
-- Output: First Name, Last Name, Title, Affected From.
-- Result contains 8 rows.

select FIRST_NAME, LAST_NAME, TITLE, AFFECTED_FROM
from worker
inner join title on title.WORKER_REF_ID = Worker.WORKER_ID
inner join Designation on Designation.ID = title.DESIGNATION_ID
where AFFECTED_FROM = (
    -- The subquery is executed for each worker, finding the maximum (latest) date that a title was assigned for that worker.
    select MAX(AFFECTED_FROM)
    from title
    where title.WORKER_REF_ID = worker.WORKER_ID
	)
order by FIRST_NAME -- Ordering by first_name 

-- 10. List all departments which have no workers assigned to them.
-- Output: Dept Name.
-- Result contains 1 row.

select distinct DEPT_NAME
from worker
right join Department on Department.ID = Worker.DEPT_ID -- Right join to include all departments and filter for those with no workers
where WORKER_ID is null

-- 11. List workers joined on the same date (without time), show new employees first.
-- Only list employees if there is at least one other employee hired on the same date.
-- Output: First Name, Last Name, Joining Date.
-- Result contains 8 rows.

select FIRST_NAME, LAST_NAME, cast(JOINING_DATE as date) AS JOINING_DATE --Using cast to convert the joining date which also contains time to just "Date" Date type which wouldn't contain time. 
from Worker
where cast(JOINING_DATE as date) IN ( 
	--The subquery groups by joining date (without time) and filters to include only dates with more than one employee 
    select cast(JOINING_DATE as date)
    from Worker
    group by cast(JOINING_DATE as date)
    having count(*) > 1
)
order by cast(JOINING_DATE as date) DESC; --sorts the output by joining date in descending order, showing newer employees first.


-- 12. List all workers who never got any bonuses, sorted by their names.
-- Output: First Name, Last Name, Joining Date.
-- Result contains 4 rows.

select distinct FIRST_NAME, LAST_NAME, JOINING_DATE
from worker
left join bonus on bonus.WORKER_REF_ID = worker.WORKER_ID
where WORKER_REF_ID is null -- Workers without bonus entries are filtered
Order by worker.FIRST_NAME, worker.LAST_NAME 

-- 13. List names of all workers with salaries above the average salary of their department.
-- Output: First Name, Last Name, Department, Salary.
-- Result contains 4 rows.

select Worker.FIRST_NAME, Worker.LAST_NAME, Department.DEPT_NAME, Worker.SALARY
from worker
join Department on Department.ID = Worker.DEPT_ID
where Worker.SALARY > (
		-- Subquery: Calculate the average salary within the worker's own department
		select avg(salary)
		from worker
		-- Match department IDs to calculate the department-specific average salary
		where worker.DEPT_ID = Department.ID
		)

-- 14. List all workers with the total bonus they have received. If no bonus, show 0.
-- Sort in decreasing order of total bonus.
-- Output: First Name, Last Name, Bonus Total.
-- Result contains 10 rows.

-- Full join and COALESCE to include all workers with or without bonuses, ordered by total
select FIRST_NAME, LAST_NAME, COALESCE(sum(Bonus.BONUS_AMOUNT), 0) as [BONUS_TOTAL]
from worker 
full join bonus on worker.WORKER_ID = bonus.WORKER_REF_ID
group by FIRST_NAME, LAST_NAME
order by [Bonus_Total] DESC

-- 15. List all workers who received more than one bonus in any given year.
-- Output: First Name, Department, Year, No Of Bonuses.
-- Result contains 2 rows.

select worker.FIRST_NAME, department.DEPT_NAME, year(bonus.BONUS_DATE) as YEAR, count(bonus.bonus_amount) as [NO_OF_BONUSES.]
from worker
join bonus on bonus.WORKER_REF_ID = worker.WORKER_ID
join Department on worker.DEPT_ID = Department.ID
group by Worker.WORKER_ID, Worker.FIRST_NAME, Department.DEPT_NAME, year(Bonus.BONUS_DATE) -- Groups by worker and year
having count(bonus.BONUS_AMOUNT) > 1  --filters to workers with multiple bonuses in a year



-- 16. List workers earning the second-highest salary in the organization.
-- Output: First Name, Last Name, Dept Name, Salary.
-- Result contains 2 rows.

--The reason I did Coalescece is cause there can exist a side-case where a worker doesn't belong to any department, so this query will make sure to not give 
-- null within the dept Name. Additionally, we do Left Join, cause there can a scenerio that worker doesn't belong to any department. 
select worker.FIRST_NAME, worker.LAST_NAME, COALESCE(DEPT_NAME, 'No Department') AS [DEPT_NAME], worker.SALARY
from worker
left join Department on worker.DEPT_ID = Department.ID
where worker.SALARY = (
    -- Finds the second-highest salary by getting the max salary below the absolute max salary.
    select max(salary)
    from worker
    where salary < (select max(salary) from worker)
	)
order by SALARY DESC


-- 17. List all workers who received bonuses in 2017 but not in 2018 with the total bonus amount (regardless of year).
-- Output: First Name, Last Name, Dept Name, Total Bonus Amount
-- Result contains 3 rows.

select FIRST_NAME, LAST_NAME, DEPT_NAME, sum(BONUS_AMOUNT) as TOTAL_BONUS_AMOUNT
from worker
join department on worker.dept_id = department.id
join bonus on worker.worker_id = bonus.worker_ref_id
group by WORKER_ID, FIRST_NAME, LAST_NAME, DEPT_NAME
-- Filters the grouped data using 'having' to apply conditions based on aggregate functions:
having sum(case when year(BONUS_DATE) = 2017 then BONUS_AMOUNT else 0 end) > 0 -- Checks if the total bonus amount for the year 2017 is greater than 0.
   and sum(case when year(BONUS_DATE) = 2018 then BONUS_AMOUNT else 0 end) = 0  -- Ensures the total bonus amount for the year 2018 is exactly 0.

-- Appendix

-- Accidentally solved question 17 to include only the sum of bonuses EXCLUSIVE to 2017
	--select 
	--	FIRST_NAME, 
	--	LAST_NAME, 
	--	COALESCE(DEPT_NAME, 'No Department') AS [DEPT_NAME],  -- Display department name; if null, label as 'No Department'
	--	COALESCE(sum(BONUS_AMOUNT), 0) as [TOTAL_BONUS_AMOUNT] -- Calculate total bonus for 2017; if no bonus, show 0
	--from worker
	--left join Department on worker.DEPT_ID = Department.ID
	--left join Bonus on worker.WORKER_ID = Bonus.WORKER_REF_ID
	--where year(BONUS_DATE) = 2017 and WORKER_ID not in (  -- Filter bonuses to include only those given in 2017 and Exclude workers who also received bonuses in 2018
	--	--Subquery returns worker IDs with bonuses in 2018
	--	select WORKER_REF_ID
	--	from Bonus
	--	where year(BONUS_DATE) = 2018
	--	)
	--group by FIRST_NAME, LAST_NAME, DEPT_NAME -- Group by worker names and department to calculate total bonuses
	--order by [TOTAL_BONUS_AMOUNT] DESC  -- Sort results by total bonus in descending order


--select * from worker
--select * from title
--select * from Department
--select * from Designation
--select * from Bonus 
--select * from Bonus 