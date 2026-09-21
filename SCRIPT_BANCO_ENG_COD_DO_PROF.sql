#DB E TABELAS DA AULA DE 11-09-26

CREATE DATABASE IF NOT EXISTS ENGENHARIA_5; 
USE ENGENHARIA_5;
DROP TABLE ENGENHEIRO_N CASCADE;
DROP TABLE PROJETO_N CASCADE;

create table ENGENHEIRO_N(id_eng INT primary key,nome_eng varchar(20)
not null,cargo varchar(15));

create table PROJETO_N(id_proj INT(10)
primary key, nome_proj varchar(25)
not null,valor_proj decimal(12,2), id_eng DECIMAL(10) references eng);

describe ENGENHEIRO_N;
describe projETO_N;

insert into ENGENHEIRO_N(id_eng,nome_eng,cargo)
values(1,'jose x','engenheiro');

SELECT * FROM ENGENHEIRO_N;
SELECT * FROM PROJETO_N;

insert into PROJETO_N(id_proj,nome_proj,valor_proj,id_eng)
values(100,'construção y',300000,1);

insert into ENGENHEIRO_N VALUES(2,'aurora','engenheiro'),(3,'maria','engenheira'),(4,'rodolfo','engenheiro');
insert into projeto_n values(101,'banheirin',20000,4),(102,'estatua da liberdade',30000009,2),(103,'buraco da rua', 20000,4),(104,'museu do bras',4000000000,2);
delete from engenheiro_n 
where id_eng = 3;
alter table projeto_n
modify nome_proj varchar(30);
Commit;
select * from ENGENHEIRO_N;
insert into engenheiro_n values(3,'maria','engenheira');
select * from PROJETO_N;
Desc engenheiro_n;
DESC PROJETO_N;
select * from engenheiro_n inner join projeto_n on engenheiro_n. id_eng=projeto_n.id_eng order by engenheiro_n. id_eng;
select * from engenheiro_n left join projeto_n on engenheiro_n. id_eng=projeto_n.id_eng order by engenheiro_n. id_eng;
select * from engenheiro_n left join projeto_n on engenheiro_n.id_eng = projeto_n.id_eng where projeto_n.id_eng is null;