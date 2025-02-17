-- YEAR_DEV = 연도별 MAX(SIZE_OF_COLONY) - SIZE_OF_COLONY
SELECT YEAR(DIFFERENTIATION_DATE) AS YEAR,
MAX(SIZE_OF_COLONY) OVER(PARTITION BY YEAR(DIFFERENTIATION_DATE)) - SIZE_OF_COLONY AS YEAR_DEV ,ID 
FROM ECOLI_DATA 
ORDER BY YEAR, YEAR_DEV