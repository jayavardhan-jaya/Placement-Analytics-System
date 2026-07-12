SELECT COUNT(*) AS Total_Students_Placed
FROM Placements;

SELECT ROUND(AVG(Salary),2) AS Average_Salary
FROM Placements;

SELECT MAX(Salary) AS Highest_Salary
FROM Placements;

SELECT MIN(Salary) AS Lowest_Salary
FROM Placements;

SELECT
Department,
COUNT(*) AS Students_Placed
FROM Students s
JOIN Placements p
ON s.Student_ID=p.Student_ID
GROUP BY Department
ORDER BY Students_Placed DESC;


SELECT

c.Company_Name,

COUNT(*) AS Total_Hires

FROM Companies c

JOIN Placements p

ON c.Company_ID=p.Company_ID

GROUP BY Company_Name

ORDER BY Total_Hires DESC;




SELECT

Company_Name,

ROUND(AVG(Salary),2) Average_Salary

FROM Companies c

JOIN Placements p

ON c.Company_ID=p.Company_ID

GROUP BY Company_Name

ORDER BY Average_Salary DESC;






SELECT

Status,

COUNT(*) Total

FROM Applications

GROUP BY Status;





SELECT

Job_Type,

COUNT(*) Total

FROM Jobs

GROUP BY Job_Type;







SELECT

Department,

ROUND(AVG(CGPA),2) Average_CGPA

FROM Students

GROUP BY Department

ORDER BY Average_CGPA DESC;









SELECT

MONTH(Placement_Date) Month,

COUNT(*) Placements

FROM Placements

GROUP BY MONTH(Placement_Date)

ORDER BY Month;







SELECT

CASE

WHEN Salary<500000 THEN 'Below 5 LPA'

WHEN Salary BETWEEN 500000 AND 800000 THEN '5-8 LPA'

ELSE 'Above 8 LPA'

END Salary_Range,

COUNT(*) Students

FROM Placements

GROUP BY Salary_Range;
