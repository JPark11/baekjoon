-- 코드를 입력하세요
SELECT member_id, member_name, gender, date_format(date_of_birth, '%Y-%m-%d') as date_of_birth
FROM member_profile
WHERE gender = 'W' and month(date_of_birth) = 3 and tlno is not null
ORDER BY member_id;