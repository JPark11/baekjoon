-- 코드를 입력하세요
SELECT a.category, sum(b.sales) as total_sales
from book a, book_sales b
where a.book_id = b.book_id 
    and b.sales_date like '2022-01%'
group by category 
order by category;
