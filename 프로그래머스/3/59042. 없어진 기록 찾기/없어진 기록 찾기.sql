-- 코드를 입력하세요
SELECT animal_id, name
from animal_outs 
where animal_id not in 
    (select animal_outs.animal_id
    from animal_outs
    join animal_ins on animal_ins.animal_id = animal_outs.animal_id);