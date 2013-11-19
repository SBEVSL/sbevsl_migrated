-- ProMol DB Setup

drop database if exists ProMol;
create database ProMol;

use ProMol;

create table structures(
id char(4),
allrun date,
jrun date,
arun date,
prun date,
nrun date,
myrun date,
motifcount integer,
constraint pk_structures primary key (id));

create table motifsets(
id varchar(40),
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
setname varchar(40),
added date,
foundin integer,
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
chain varchar(40),
name char(3),
number varchar(40),
resultid bigint,
constraint pk_rs primary key (id),
constraint fk_result foreign key (resultid) references results (id));

alter table resultspecs auto_increment = 1;

create table resultrmsd(
id bigint auto_increment,
total decimal(6,4),
alpha decimal(6,4),
alpha_beta decimal(6,4),
resultid bigint,
constraint pk_rmsd primary key (id),
constraint fk_resultsource foreign key (resultid) references results (id));

alter table resultrmsd auto_increment = 1;

create table credentials(
user varchar(40),
password varchar(50),
permissions integer,
constraint pk_creds primary key (user));

insert into credentials values ('FILL_IN-Username', AES_ENCRYPT('FILL_IN-Password', 'FILL_IN-EncryptionKey'), 2);

create table sessions(
token char(36),
account varchar(40),
born datetime,
expires datetime,
constraint pk_sess primary key (token),
constraint fk_sess foreign key (account) references credentials (user));
