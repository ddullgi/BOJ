-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(*) AS count FROM ANIMAL_INS 
GROUP BY ANIMAL_TYPE
having animal_type in ('cat', 'dog')
ORDER BY ANIMAL_TYPE 