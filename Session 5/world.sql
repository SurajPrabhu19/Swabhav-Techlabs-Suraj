
create DATABASE if NOT EXISTS SWABHAV;
USE SWABHAV;
SHOW TABLES;



CREATE TABLE if NOT EXISTS Employee_1(
id INT PRIMARY KEY ,
e_name VARCHAR(20) NOT NULL,
dept VARCHAR(10) NOT NULL ,
addr VARCHAR(20) 
);

CREATE TABLE if NOT EXISTS Dept_1(
dept VARCHAR(10) ,
dept_id INT NOT NULL  ,
salary INT

);

ALTER TABLE Dept_1
ADD FOREIGN KEY (dept_id) REFERENCES Employee_1(id);

DESCRIBE employee_1;

DESCRIBE Dept_1;

INSERT INTO Employee_1 VALUES ('1713122', 'Amir', 'Extc' , 'Mumbai');

SELECT * FROM Employee_1;
SELECT * FROM Dept_1;

pyinternpyintern