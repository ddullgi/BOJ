SELECT FO.PRODUCT_ID, FP.PRODUCT_NAME, SUM(FO.AMOUNT) * FP.PRICE AS TOTAL_SALES
FROM FOOD_ORDER AS FO
    INNER JOIN FOOD_PRODUCT AS FP
    ON FO.PRODUCT_ID = FP.PRODUCT_ID
WHERE (FO.PRODUCE_DATE >= '2022-04-30' AND FO.PRODUCE_DATE < '2022-06-01')
GROUP BY FO.PRODUCT_ID, FP.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, FO.PRODUCT_ID ASC;