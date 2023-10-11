-- 코드를 입력하세요
SELECT P.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE AS P JOIN REST_REVIEW AS R
ON P.MEMBER_ID = R.MEMBER_ID
WHERE P.member_id = (SELECT R.member_id
                        FROM REST_REVIEW AS R
                        GROUP BY R.member_id
                        ORDER BY COUNT(*) DESC
                        LIMIT 1)
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT