from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]   # x(열)
dy = [0,0,1,-1]   # y(행)

def bfs(y, x):  # (행, 열)
    q = deque()
    q.append((y, x))
    graph[y][x] = 0  # 방문 처리

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((ny, nx))

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())   # M=가로(열), N=세로(행)
    graph = [[0]*M for _ in range(N)]     # N x M

    for _ in range(K):
        x, y = map(int, input().split())  # (열, 행)
        graph[y][x] = 1

    cnt = 0
    for i in range(N):        # 행
        for j in range(M):    # 열
            if graph[i][j] == 1:
                bfs(i, j)     # (행, 열)
                cnt += 1
    print(cnt)



from collections import deque


dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[y][x] = 0  # 방문처리
    
    while queue:
        y,x= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or nx >=M or ny <0 or ny>=N:
                continue
            # if graph[nx][ny]==0:
            #     continue
            if graph[ny][nx]==1:
                # 1일때(배추가심어진부분), 어떻게 처리를 해야하지
                graph[ny][nx] = 0
                queue.append((ny,nx))
    
T=int(input())

for _ in range(T):
    # 가로 M, 세로 N, K는 배추가 심어진 위치의 개수
    # M이 가로줄 수가 아니고 가로 길이였네..
    # 세로도 마찬가지..
    # 즉 N이 행, M이 열
    M, N, K = map(int, input().split())
    #graph = [[0 for _ in range(M)] for _ in range(N)]
    graph = [[0]*M for _ in range(N)] 
    for _ in range(K):
        x, y = map(int , input().split())
        graph[y][x] = 1
        
    # for i in graph:
    #     print(*i)

    ## 그래프 완료
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt +=1

    print(cnt)