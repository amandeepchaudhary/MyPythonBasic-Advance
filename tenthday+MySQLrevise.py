#linspace()
#revising MySQL
'''
show databases;
use database_name;
select database();
show tables;
if wanna open the tabel and see the fields then===
desc table_name;
if wanna see the content inn tables==
select * from table_name;
delete the database==
drop database_name;
delete the table==
drop table table_name;
creating database==
create database database_name;
create table==
create table table_name
(id int not null auto_increment primary key,name varchar(1-255) not null deafault 'noname');
if you forget to add a field/column then==
alter 
alter table_name 
add column phone double not null deafault 0;
if you want to delete a table column==
alter table table_name
drop column column_name ;
inserting data in tabel==
insert into table_name
(fields=name,age)
values('aman',22);
to modify a data==
update tabel_name set name ='ishu' where id=1;
some methods==
select max(field) from table_name; --for maximum number
select min(field) from table_name; --for minimum number
select avg(field) from table_name; --for avg of the number
select sum(field) from table_name; --for sum of the numbers in table
select upper(field) from table_name; --for uppercase of the numbers in table
select lower(field) from table_name; --for lowercase of the numbers in table
primary key and foreign key====
create table table_name1
(id int not null auto_increment primary key,name varchar(1-255) not null deafault 'noname');
create table table_name2
(oid int not null auto_increment ,nid int not null default 000,foreign key(nid) references table_name1(id),name varchar(1-255) not null deafault 'noname');
joins===
inner join ==
select * from table_name1 
join table_name2,
on table_name1.id = table_name2.nid; --in this the mutual data shows which is present on both the tables 

left join==
select * from table_name1 left join table_name2,
on table_name1.id = tabvel_name2.nid; --in this the 1st table's all data shows even if it is not available on the second one

right join==
select * from table_name1 right join table_name2,
on table_name1.id=table_name2.nid; --in this the data which is present on the table_name2 takes priority and shows 
                                   --all wheater it is related to the table_name1 or not

'''
