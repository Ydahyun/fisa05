N, M = map(int,input().split()) # N X M 지도

arr = [list(map(int,list(input()))) for _ in range(N)] # N번동안 반복(N개의 ROWS)

def bfs():
    q = []
    q.append((0,0)) # 초기 좌표
    while q:
        ci, cj = q.pop(0)
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]: # 4방향에 대하여
            ni, nj = ci+di, cj+dj # 다음 위치의 좌표 (ni,nj)
            if 0<=ni < N and 0 <= nj < M: # 범위 내 좌표라면
                if arr[ni][nj] == 1: # 아직 가지 않은 곳이라면(현재 상태가 1이라면 다른 어떤 노드에서도 아직 방문 X)
                    q.append((ni,nj)) # 큐에 삽입
                    arr[ni][nj] = arr[ci][cj] + 1 # 현재 노드까지의 거리 + 1

bfs() # bfs로 표시
print(arr[N-1][M-1]) # 맨 끝점의 값 출력