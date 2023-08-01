CREATE VIEW view1 AS
SELECT 
reports.task_id AS id,
AVG(reports.score) AS average
FROM reports
GROUP BY reports.task_id;

______________________________________

CREATE VIEW view2 AS
SELECT view1.id as id,
    CASE
        WHEN average <=20
            THEN 'Hard'
        WHEN average >20 AND average <=60
            THEN 'Medium'
        WHEN average > 60
            THEN 'Easy'
    END AS difficulty
FROM view1;
______________________________________

SELECT 
tasks.id AS task_id,
tasks.name AS task_name,
view2.difficulty AS difficulty
FROM tasks
INNER JOIN view2 ON view2.id = tasks.id
ORDER BY tasks.id;


