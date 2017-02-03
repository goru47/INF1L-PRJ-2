DROP TABLE IF EXISTS scoreboard;

create table scoreboard (naam varchar(20), score integer);

insert into scoreboard(naam,score) values
('Han', 50);

select * from scoreboard