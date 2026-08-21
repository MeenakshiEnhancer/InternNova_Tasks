create database student_data;

use student_data;

create table Students(
std_name varchar(50),
rollno int,
age int,
marks decimal(3,1),
grade char(1)
);

insert into Students (std_name,rollno,age,marks,grade)
values ("Ganesha",101,18,90.5,'A'),
("Priya",102,19,80,'B'),
("Ram",103,21,75.5,'C'),
("Madhu",107,18,81,'B'),
("Radha",105,19,90,'A'),
("Meera",108,18,92,'A');

select * from Students;

select std_name,rollno,marks from Students;

select std_name as student_name,
marks as Score
from Students;