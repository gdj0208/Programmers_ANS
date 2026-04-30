

def solution(wallpaper):
    answer = []

    height = len(wallpaper)
    width = len(wallpaper[0])

    min_x, max_x = width, 0
    min_y, max_y = height, 0
    

    for y in range(height):
        for x in range(width) :
            if wallpaper[y][x] == '.' :
                continue

            min_x = x if x < min_x else min_x
            min_y = y if y < min_y else min_y
            max_x = x if max_x < x else max_x
            max_y = y if max_y < y else max_y

    answer =[min_y, min_x, max_y+1, max_x+1]
    return answer

"""
# 추천 답안
def solution(wallpaper):
    # '#'가 있는 모든 좌표의 y, x를 각각 리스트로 모읍니다.
    y_indices = [y for y, row in enumerate(wallpaper) for x, val in enumerate(row) if val == '#']
    x_indices = [x for y, row in enumerate(wallpaper) for x, val in enumerate(row) if val == '#']

    # 최소/최대 좌표를 찾아 결과 형식을 맞춥니다.
    return [min(y_indices), min(x_indices), max(y_indices) + 1, max(x_indices) + 1]
"""

wallpaper = ["..", "#."]
print(solution(wallpaper))