DROP DATABASE IF EXISTS placement_analytics;

CREATE DATABASE placement_analytics;

USE placement_analytics;

-- =====================================================
-- Students
-- =====================================================

CREATE TABLE Students (

    Student_ID INT PRIMARY KEY,

    Name VARCHAR(100) NOT NULL,

    Gender ENUM('Male','Female'),

    Department VARCHAR(50) NOT NULL,

    Graduation_Year YEAR NOT NULL,

    CGPA DECIMAL(3,2) NOT NULL

);

-- =====================================================
-- Companies
-- =====================================================

CREATE TABLE Companies (

    Company_ID INT PRIMARY KEY,

    Company_Name VARCHAR(100) NOT NULL,

    Industry VARCHAR(100),

    Location VARCHAR(100)

);

-- =====================================================
-- Jobs
-- =====================================================

CREATE TABLE Jobs (

    Job_ID INT PRIMARY KEY,

    Company_ID INT NOT NULL,

    Job_Role VARCHAR(100) NOT NULL,

    Salary_Offered INT NOT NULL,

    Job_Type ENUM('Full-Time','Internship'),

    CONSTRAINT FK_Jobs_Companies
    FOREIGN KEY (Company_ID)
    REFERENCES Companies(Company_ID)

);

-- =====================================================
-- Applications
-- =====================================================

CREATE TABLE Applications (

    Application_ID INT PRIMARY KEY,

    Student_ID INT NOT NULL,

    Job_ID INT NOT NULL,

    Application_Date DATE,

    Status ENUM('Applied','Selected','Rejected','Pending'),

    CONSTRAINT FK_Applications_Students
    FOREIGN KEY(Student_ID)
    REFERENCES Students(Student_ID),

    CONSTRAINT FK_Applications_Jobs
    FOREIGN KEY(Job_ID)
    REFERENCES Jobs(Job_ID)

);

-- =====================================================
-- Placements
-- =====================================================

CREATE TABLE Placements (

    Placement_ID INT PRIMARY KEY,

    Student_ID INT NOT NULL,

    Company_ID INT NOT NULL,

    Job_ID INT NOT NULL,

    Placement_Date DATE,

    Salary INT,

    CONSTRAINT FK_Placements_Students
    FOREIGN KEY(Student_ID)
    REFERENCES Students(Student_ID),

    CONSTRAINT FK_Placements_Companies
    FOREIGN KEY(Company_ID)
    REFERENCES Companies(Company_ID),

    CONSTRAINT FK_Placements_Jobs
    FOREIGN KEY(Job_ID)
    REFERENCES Jobs(Job_ID)

);