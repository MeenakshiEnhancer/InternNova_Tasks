select * from students;

use student_data;

#Courses table
create table courses(
rollno int,
course varchar(50),
department varchar(50)
);

insert into courses (rollno,course,department)
values(101,"AI","CSE"),
(102,"DS","ECE"),
(103,"Python","EEE"),
(104,"Java","Mech"),
(105,"ML","CSE"),
(106,"AIML","ECE"); 

select * from courses;

#Inner Join
select s.std_name ,s.rollno,c.course,c.department from students as s
inner join courses as c
on s.rollno=c.rollno;

#left join
select s.std_name,s.rollno,c.course from students as s
left join courses as c
on s.rollno=c.rollno;

#Right join
select s.std_name,c.course from students as s
right join courses as c
on s.rollno=c.rollno;

