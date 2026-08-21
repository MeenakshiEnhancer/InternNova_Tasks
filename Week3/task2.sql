/*Filter records using the WHERE clause.
Use comparison operators in conditions.
Sort records using ORDER BY.
Perform calculations using aggregate functions:
COUNT()
SUM()
AVG()
MIN()
MAX() */

use student_data;
select * from students;

#Filter records using the WHERE clause.

select std_name,age from students
where age=18;

select std_name,grade from students
where grade between 'A'and 'C';

# Use comparison operators in conditions.
select std_name,marks from students
where marks<=80;

# Sort records using ORDER BY.
select * from students
order by marks desc;

select std_name,age from students
order by age;

#Perform calculations using aggregate functions:

select count(*) as total_strength from students;

select sum(marks) as total_marks from students;

select round(avg(marks),2) as avg_marks from students;

select min(age) as minimum_age from students;

select max(age) as maximum_age from students;