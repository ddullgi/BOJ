-- 코드를 입력하세요
SELECT BOOK_ID, TO_CHAR(PUBLISHED_DATE, 'YYYY-MM-DD') AS PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY = '인문' AND TO_CHAR(PUBLISHED_DATE, 'YYYY-MM-DD') LIKE '2021%'
ORDER BY PUBLISHED_DATE