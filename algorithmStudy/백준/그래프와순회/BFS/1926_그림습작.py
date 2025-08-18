import sys
from collections import deque

input = sys.stdin.readline

n,m=map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

# print(graph)

visited = [[0]*m for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y,visited):
    queue = deque()
    queue.append((x,y))
    cnt=0

    while queue:
        x,y = queue.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))
        cnt+=1
    return cnt


ans=[]
for i in range(n):      
    for j in range(m):    
        if graph[i][j] == 1 and visited[i][j] == 0:
            ans.append(bfs(i, j, visited))     

if len(ans)==0:
    print(0)
    print(0)
else:
    print(len(ans))
    print(max(ans))