from collections import deque

N = int(input())

graph = []

# 지도(맵) 그리기
for _ in range(N):
    graph.append(list(map(int, input())))

# 방문 체커 맵 그리기 - 정사각형 임
visited = [[False] * N for _ in range(N)]

def BFS(x, y):
    # 이동할 상하좌우 방향 저으이
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))
    d=0  # 단면적을 셀 변수
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 위치 벗어나면 안되므로 조건 추가
            if nx<0 or nx>=N or ny <0 or ny >=N:
                continue
            # 벽이므로 진행 불가 또는 이미 방문 지역인 경우
            if graph[nx][ny]==0 or visited[nx][ny]==True:
                continue

            if graph[nx][ny]==1 and visited[nx][ny]==False:
                queue.append((nx,ny))
                visited[nx][ny] = True
                d += 1
    gaduri = 1
    return d

dan_myunjuk = []
for i in range(N):
    for j in range(N):
        dan_myunjuk.append(BFS(i,j))
