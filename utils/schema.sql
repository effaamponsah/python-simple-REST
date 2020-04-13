drop table if exists students;

create table students(
    student_id serial primary key,
    student_name text not null,
    gender text not null
);

insert into students (student_name, gender) values('John Doe', 'Male');
insert into students (student_name, gender) values('Jane Doe', 'Female');
insert into students (student_name, gender) values('William Shakespeare', 'Male');