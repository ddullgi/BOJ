-- 코드를 입력하세요
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I, ANIMAL_OUTS O
WHERE I.ANIMAL_ID = O.ANIMAL_ID 
ORDER BY O.DATETIME - I.DATETIME DESC
FETCH FIRST 2 ROWS ONLY