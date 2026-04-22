SELECT
    USER_ID, 
    PRODUCT_ID
from
    ONLINE_SALE
group by
    USER_ID, PRODUCT_ID
having 
    count(distinct ONLINE_SALE_ID) > 1
order by
    USER_ID ASC,
    PRODUCT_ID DESC