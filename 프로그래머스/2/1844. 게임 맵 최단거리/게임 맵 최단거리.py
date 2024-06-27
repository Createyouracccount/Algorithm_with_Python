# from collections import deque

# def solution(maps):
#     n, m = len(maps), len(maps[0])
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
#     # BFS 사용
#     queue = deque([(0, 0)])
#     maps[0][0] = 1  # 시작 지점
    
#     while queue:
#         x, y = queue.popleft()
        
#         # 상대 팀 진영에 도착한 경우
#         if x == n - 1 and y == m - 1:
#             return maps[x][y]
        
#         # 네 방향으로 이동
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
            
#             # 유효한 위치인지 확인
#             if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
#                 queue.append((nx, ny))
#                 maps[nx][ny] = maps[x][y] + 1
    
#     # 상대 팀 진영에 도달할 수 없는 경우
#     return -1


from collections import deque

def solution(maps):
    # 초기화
    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    dist = [[0] * len(maps[0]) for _ in range(len(maps))]

    cx, cy = 0, 0
    dist[cx][cy] = 1
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))  # 큐에 시작 위치를 추가

    row = len(maps)  # 가로 크기
    col = len(maps[0])  # 세로 크기
    answer = -1  # 초기값, 목적지에 도달하지 못할 경우를 대비해 설정

    # 목적지는 맵의 우측 하단
    while q:
        cx, cy = q.popleft()  # 큐의 앞에서 위치를 꺼냄
        if cx == row - 1 and cy == col - 1:  # 목적지에 도달하면
            answer = dist[cx][cy]
            break
        for i in range(4):
            nx, ny = cx + x[i], cy + y[i]
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            if visited[nx][ny] == 1 or maps[nx][ny] == 0:
                continue
            q.append((nx, ny))
            visited[nx][ny] = 1
            dist[nx][ny] = dist[cx][cy] + 1

    return answer

# 테스트 예제
maps = [
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

print(solution(maps))

