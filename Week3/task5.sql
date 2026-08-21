#Subqueries
#Find students scoring above the average marks

select * from students;

select std_name,marks from students
where marks >(
select avg(marks) as avg_marks from students);

#Find students who have the highest marks

select std_name,marks from students
where marks = (select max(marks) from students);
 