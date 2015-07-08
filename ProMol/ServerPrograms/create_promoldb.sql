-- ProMol DB Setup

drop database if exists ProMol;
create database ProMol;

use ProMol;

create table structures(
id varchar(8),
rdate varchar(35),
motifcount integer,
constraint pk_structures primary key (id));

create table motifsets(
id varchar(10),
motifcount integer,
modified date,
constraint pk_motifsets primary key (id));

insert into motifsets values 
('J Set', 0, curdate()),
('A Set', 0, curdate()),
('P Set', 0, curdate()),
('N Set', 0, curdate()),
('User Set', 0, curdate());

create table motifs(
id varchar(40),
setname varchar(10),
added date,
foundin integer,
EC1 varchar(5),
EC2 varchar(5),
EC3 varchar(5),
EC4 varchar(5),
constraint pk_motifs primary key (id),
constraint fk_set foreign key (setname) references motifsets (id));

create table results(
id bigint auto_increment,
pdbid char(4),
motif varchar(40),
pf double(3, 2),
version double(2, 1),
result varchar(7),
date date,
constraint pk_results primary key (id),
constraint fk_pdbid foreign key (pdbid) references structures (id),
constraint fk_motif foreign key (motif) references motifs (id));

alter table results auto_increment = 1;

create table resultspecs(
id bigint auto_increment,
residues varchar(40),
total decimal(6,4),
alpha decimal(6,4),
alpha_beta decimal(6,4),
constraint pk_rs primary key (id),
constraint fk_result foreign key (id) references results (id));

alter table resultspecs auto_increment = 1;

create table credentials(
user varchar(40),
password varchar(50),
permissions integer,
constraint pk_creds primary key (user));


