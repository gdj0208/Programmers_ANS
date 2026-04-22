from collections import deque

def solution(m, n, h, w, drops):
    # 떨어지지 않는 곳(0)은 무한대(가장 늦은 시간)로 취급하여 탐색 로직 단순화
    INF = len(drops) + 1
    mat = [[INF for _ in range(n)] for _ in range(m)]

    # drop 위치 마킹 (1부터 시작)
    for i, (y, x) in enumerate(drops):
        mat[y][x] = i + 1

    # 1단계: 가로 방향(행 단위)으로 크기 W의 슬라이딩 윈도우 최솟값 구하기
    row_min = [[0] * (n - w + 1) for _ in range(m)]
    
    for r in range(m):
        q = deque()
        for c in range(n):
            # 윈도우 범위를 벗어난 인덱스 제거
            if q and q[0] <= c - w:
                q.popleft()
            
            # 현재 값보다 큰 값들은 최솟값이 될 가능성이 없으므로 제거 (단조 증가 유지)
            while q and mat[r][q[-1]] >= mat[r][c]:
                q.pop()
                
            q.append(c)
            
            # 윈도우 크기가 W에 도달한 시점부터 최솟값 저장
            if c >= w - 1:
                row_min[r][c - w + 1] = mat[r][q[0]]

    # 2단계: 세로 방향(열 단위)으로 크기 H의 슬라이딩 윈도우 최솟값 구하기
    width = n - w + 1
    height = m - h + 1
    final_min = [[0] * width for _ in range(height)]
    
    for c in range(width):
        q = deque()
        for r in range(m):
            if q and q[0] <= r - h:
                q.popleft()
                
            while q and row_min[q[-1]][c] >= row_min[r][c]:
                q.pop()
                
            q.append(r)
            
            if r >= h - 1:
                final_min[r - h + 1][c] = row_min[q[0]][c]

    # 3단계: 최적의 위치(최솟값이 가장 큰 윈도우) 찾기
    # 기존 코드와 동일한 순회 순서를 사용하여 동일한 조건 시 y, x가 작은 순서 보장
    max_val = 0
    ans_y, ans_x = 0, 0
    
    for y in range(height):
        for x in range(width):
            if max_val < final_min[y][x]:
                max_val = final_min[y][x]
                ans_y = y
                ans_x = x

    return [ans_y, ans_x]