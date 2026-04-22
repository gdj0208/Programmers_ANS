select
    count(n_info.FISH_NAME) as FISH_COUNT
from
    FISH_INFO as info
    left join FISH_NAME_INFO as n_info on info.FISH_TYPE = n_info.FISH_TYPE
where
    n_info.FISH_NAME = "BASS" or n_info.FISH_NAME = "SNAPPER"