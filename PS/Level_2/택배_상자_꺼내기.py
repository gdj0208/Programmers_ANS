
def solution(n, w, num) :
    answer = 0
    
    def get_xy(number, width) :
        number -= 1 
        y = number // width
        x = number % width
        
        if y % 2 == 1:
            x = (width - 1) - x
        return x, y

    sx, sy = get_xy(num, w)
    ex, ey = get_xy(n, w)

    answer = ey - sy + 1

    if ey % 2 == 0:
        top_box_num = ey * w + sx + 1
    else:
        top_box_num = ey * w + (w - 1 - sx) + 1
        
    if top_box_num > n:
        answer -= 1

    return answer
