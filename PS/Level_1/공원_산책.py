
WIDTH, HEIGHT = 0, 0

def get_start_loc(park) :
    y = 0
    for row in park :
        x = 0
        for unit in row :
            if unit == 'S':
                start_x, start_y = x, y
                return start_x, start_y
            x += 1
        y += 1
    return 0,0

def is_out_of_map(x, y) :
    global WIDTH, HEIGHT
    return x < 0 or WIDTH <= x or y < 0 or HEIGHT <= y

def can_move(park, loc, op, dist) :
    x, y = loc[0], loc[1]
    for i in range(dist) :
        if op == "N" :
            y -= 1
        elif op == "S" : 
            y += 1
        elif op == "W" :
            x -= 1 
        elif op == "E" :
            x += 1

        if is_out_of_map(x, y) :
            return False
        
        if park[y][x] == 'X' :
            return False
        
    return True
        

def move(park, loc, order) :
    op, dist = order.split()
    dist = int(dist)
    x, y = loc[0], loc[1]

    if can_move(park, loc, op, dist) == False :
        return loc[0], loc[1]

    if op == "N" :
        y -= dist
    elif op == "S" : 
        y += dist
    elif op == "W" :
        x -= dist
    elif op == "E" :
        x += dist

    return x, y

def solution(park, routes):
    global WIDTH, HEIGHT
    answer = []

    HEIGHT = len(park)
    WIDTH = len(park[0])

    x, y = get_start_loc(park)
    for order in routes :
        x, y = move(park, [x, y], order)

    return [y, x]

park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]
print(solution(park, routes))