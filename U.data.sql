CREATE DATABASE USER ;
use USER;
 CREATE TABLE REGES(
 U_id INT NOT NULL,
 U_First_Name varchar(100) NOT NULL,
 U_Middle_Name varchar(100) ,
 U_Last_Name varchar(100) ,
 U_Email varchar(100) NOT NULL,
 U_Ph_No varchar(100) NOT NULL,
 U_password varchar(100) NOT NULL,
 
 PRIMARY KEY (U_id)
 );
 Select * from REGES ;