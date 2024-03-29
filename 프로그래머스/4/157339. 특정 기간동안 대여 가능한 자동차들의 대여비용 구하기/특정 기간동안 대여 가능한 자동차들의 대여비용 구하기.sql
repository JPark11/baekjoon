select c.car_id, c.car_type, round(c.daily_fee * 30 * (100 - d.discount_rate)/100,0) as fee
from car_rental_company_car c
inner join (select distinct car_id
            from car_rental_company_rental_history
            where car_id not in (select distinct car_id
                                 from car_rental_company_rental_history 
                                 where start_date < '2022-11-01' and end_date >= '2022-11-01' or start_date >= '2022-11-01' and start_date <= '2022-11-30')) h
on c.car_id = h.car_id
inner join (select car_type, discount_rate 
           from car_rental_company_discount_plan 
           where duration_type = '30일 이상') d
on c.car_type = d.car_type 
where c.car_type in ('세단', 'SUV') 
and round(c.daily_fee * 30 * (100 - d.discount_rate)/100,0) between 500000 and 1999999
order by fee desc, c.car_type, car_id desc;