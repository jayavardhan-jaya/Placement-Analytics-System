CREATE DATABASE placement_analytics;

USE placement_analytics;

CREATE TABLE students(
student_id INT PRIMARY KEY,
name VARCHAR(100),
gender VARCHAR(20),
department VARCHAR(50),
graduation_year INT,
cgpa DECIMAL(3,2)
);

CREATE TABLE companies(
company_id INT PRIMARY KEY,
company_name VARCHAR(100),
industry VARCHAR(100),
location VARCHAR(100)
);

CREATE TABLE jobs(
job_id INT PRIMARY KEY,
company_id INT,
job_role VARCHAR(100),
salary_offered INT,
job_type VARCHAR(50),
FOREIGN KEY(company_id)
REFERENCES companies(company_id)
);

CREATE TABLE applications(
application_id INT PRIMARY KEY,
student_id INT,
job_id INT,
application_date DATE,
status VARCHAR(50),
FOREIGN KEY(student_id)
REFERENCES students(student_id),
FOREIGN KEY(job_id)
REFERENCES jobs(job_id)
);

CREATE TABLE placements(
placement_id INT PRIMARY KEY,
student_id INT,
company_id INT,
job_id INT,
placement_date DATE,
salary INT
);