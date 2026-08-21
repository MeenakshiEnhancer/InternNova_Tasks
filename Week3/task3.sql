select * from students;

#Group records using GROUP BY.

#Counting number of students are in each grade:
select grade,count(std_name) as count from students
group by grade;

# Aggregate value for each group
# Find the average marks for each grade
select grade,round(avg(marks),2) as average_marks from students
group by grade;

#Use the HAVING clause to filter grouped results.
# display only grades where the average marks are above 85
select grade,avg(marks) as avg_marks from students
group by grade
having avg_marks>85;