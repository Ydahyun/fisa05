from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 경로 벗어나는 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 0을 만난 경우
            if graph[nx][ny] == 0:
                continue

            # 1을 만난 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]


N, M = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

print(bfs(0,0))