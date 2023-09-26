-- 코드를 입력하세요
SELECT A.CATEGORY, SUM(B.SALES) AS TOTAL_SALES
FROM BOOK AS A JOIN BOOK_SALES AS B
ON A.BOOK_ID = B.BOOK_ID
WHERE B.SALES_DATE LIKE '2022-01%'
GROUP BY A.CATEGORY
ORDER BY A.CATEGORY