from collections import deque

#N, M = map(int, input().split())

graph = []

#for _ in range(N):
#    graph.append(list(map(int, input())))
#print(graph)
N=4
M=6
graph = [[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]]

# visited = [False] * n
# visited = [[False] * m for _ in range(n)]

def BFS(x, y):
    # 이동할 상, 하, 좌, 우 방향 정의
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y,0))
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True

    while queue:
        x, y, d = queue.popleft()
        if (x, y) == (n - 1, n -1):
            return d
        # 현재 위치에서 4가지 방향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 위치 벗어나면 안되므로 조건 추가
            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            # 벽이므로 진행 불가
            if graph[nx][ny]==0:
                continue
            # 벽이 아니므로 이동 가능
            # if graph[nx][ny]==1:
            #     graph[nx][ny] = graph[x][y]+1
            #     queue.append((nx,ny))
            queue.append((nx, ny, d + 1))
            visited[nx][ny] = True

    # 마지막 값에서 카운트 값 뽑기
    return graph[N-1][M-1]

print(BFS(0,0))