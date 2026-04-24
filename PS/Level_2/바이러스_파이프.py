from collections import deque

def solution(n, infection, edges, k):
    # 1. 인접 리스트 형식으로 그래프 구성
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, p_type in edges:
        graph[u].append((v, p_type))
        graph[v].append((u, p_type))

    max_infected = 0

    # 2. DFS (K번의 파이프 선택 시뮬레이션)
    def dfs(current_k, infected_nodes):
        nonlocal max_infected
        
        # 종료 조건: k번 파이프를 모두 골랐다면 갱신
        if current_k == 0:
            max_infected = max(max_infected, len(infected_nodes))
            return

        # 3. 파이프 종류 1, 2, 3 각각에 대해 시뮬레이션
        for p_type in range(1, 4):
            # 이번 턴의 감염 상태를 담을 set
            new_infected = set(infected_nodes)
            
            # BFS를 위한 큐 생성 (현재 감염된 모든 노드를 큐에 넣고 시작)
            queue = deque(infected_nodes)
            
            # 4. 선택한 파이프(p_type)를 타고 갈 수 있는 데까지 모두 탐색 (BFS)
            while queue:
                curr = queue.popleft()
                
                for neighbor, edge_type in graph[curr]:
                    # 선택한 파이프 종류와 일치하고, 아직 이번 턴에 방문(감염)하지 않은 노드라면
                    if edge_type == p_type and neighbor not in new_infected:
                        new_infected.add(neighbor)
                        queue.append(neighbor) # 연쇄 감염을 위해 큐에 추가
            
            # 다음 턴으로 재귀 호출 (파이프 선택 횟수 1 감소, 새롭게 갱신된 감염 상태 전달)
            dfs(current_k - 1, new_infected)

    # 5. 초기 상태 실행
    dfs(k, {infection})

    return max_infected


# 테스트 실행
n = 7
infection = 6
edges = [[1, 2, 3], [1, 4, 3], [4, 5, 1], [5, 6, 1], [3, 6, 2], [3, 7, 2]]
k = 3
print(solution(n, infection, edges, k))