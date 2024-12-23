-- 코드를 입력하세요
SELECT
    CONCAT(CONCAT(
    	CONCAT(CONCAT(CONCAT('/home/grep/src/', B.BOARD_ID),'/'),file_id), 
    FILE_NAME),file_ext) AS FILE_PATH
FROM (
    SELECT
        BOARD_ID
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    FETCH NEXT 1 ROWS ONLY
) B JOIN USED_GOODS_FILE F ON B.BOARD_ID = F.BOARD_ID
ORDER BY F.FILE_ID DESC