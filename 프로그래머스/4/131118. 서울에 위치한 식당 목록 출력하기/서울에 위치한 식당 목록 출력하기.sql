-- 코드를 입력하세요
SELECT a.rest_id, a.rest_name, a.food_type, a.favorites, a.address, coalesce(round(avg(b.review_score), 2), 0) as score
from rest_info a
inner join rest_review b
on a.rest_id = b.rest_id
where a.address like '서울%'
group by a.rest_id 
order by score desc, a.favorites desc;