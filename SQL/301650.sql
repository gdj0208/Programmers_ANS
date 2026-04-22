WITH 
FirstGen as (
    SELECT *
    FROM ECOLI_DATA
    WHERE PARENT_ID is NULL
),
SecondGen as (
    SELECT child.*
    FROM ECOLI_DATA as child
    INNER JOIN FirstGen as parent on parent.ID = child.PARENT_ID
),
ThirdGen as (
    SELECT child.*
    FROM ECOLI_DATA as child
    INNER JOIN SecondGen as parent on parent.ID = child.PARENT_ID
)
SELECT ID
FROM ThirdGen
ORDER BY ID ASC