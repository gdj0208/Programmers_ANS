with biggest as (
select
    n_info.FISH_NAME,
    MAX(info.LENGTH) as LENGTH
from
    FISH_INFO as info
    left join FISH_NAME_INFO as n_info on info.FISH_TYPE = n_info.FISH_TYPE
group by 
    n_info.FISH_NAME
)
select
    info.ID,
    n_info.FISH_NAME,
    info.LENGTH
from
    FISH_INFO as info
    left join FISH_NAME_INFO as n_info on info.FISH_TYPE = n_info.FISH_TYPE
    left join biggest on n_info.FISH_NAME = biggest.FISH_NAME
where
    n_info.FISH_NAME = biggest.FISH_NAME and
    info.LENGTH = biggest.LENGTH