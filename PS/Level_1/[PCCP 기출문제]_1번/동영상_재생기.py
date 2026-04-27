
def convert_time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    total_seconds = (minutes * 60) + seconds
    return total_seconds

def convert_seconds_to_time(total_seconds):
    minutes, seconds = divmod(total_seconds, 60)
    time_str = f"{minutes:02d}:{seconds:02d}"
    return time_str

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''

    total_len = convert_time_to_seconds(video_len)
    cur_time = convert_time_to_seconds(pos)
    start = convert_time_to_seconds(op_start)
    end = convert_time_to_seconds(op_end)

    if start <= cur_time and cur_time <= end :
        cur_time = end

    for command in commands : 
        if command == "prev" :
            cur_time = cur_time - 10 if 0 < cur_time-10 else 0 
        elif command == "next" :
            cur_time = cur_time+10 if 0 < cur_time+10 else 0

        if start <= cur_time and cur_time <= end :
            cur_time = end
        
        if total_len < cur_time:
            cur_time = total_len

    answer = convert_seconds_to_time(cur_time)
    return answer