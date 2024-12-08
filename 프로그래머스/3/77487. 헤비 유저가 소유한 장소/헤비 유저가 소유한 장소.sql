-- 코드를 입력하세요
SELECT A.*
  FROM PLACES A
 WHERE EXISTS (SELECT COUNT(A.ID) AS ID
                    , A.HOST_ID AS HOST_ID
                 FROM PLACES B
                WHERE A.HOST_ID = B.HOST_ID
                GROUP BY HOST_ID
               HAVING COUNT(A.ID) >= 2)