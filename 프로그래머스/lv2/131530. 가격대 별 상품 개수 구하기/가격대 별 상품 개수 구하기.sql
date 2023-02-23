-- 코드를 입력하세요
SELECT (
    case
        when price < 10000 then 0
        else truncate(price, -4)
        end) PRICE_GROUP,count(product_id) PRODUCTS
from product
group by price_group
order by price_group