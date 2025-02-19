-- 코드를 작성해주세요
SELECT G.SCORE, E.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM 
    HR_EMPLOYEES E,
    (
        SELECT EMP_NO, YEAR, SUM(SCORE) SCORE
        FROM HR_GRADE 
        GROUP BY EMP_NO, YEAR
    ) G
WHERE  
    E.EMP_NO = G.EMP_NO AND
    G.YEAR = '2022'
ORDER BY G.SCORE DESC
LIMIT 1