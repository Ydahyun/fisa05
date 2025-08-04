import sys
from collections import deque
input=sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for neighbours in graph:
    neighbours.sort(reverse=True)


visited = [0]*(N+1)
cnt = 1

def bfs(graph, R, visited):
    global cnt
    q = deque([R])  
    visited[R] = cnt  # 현재 노드를 방문 처리
    cnt +=1

    while q:
        v = q.popleft()
        for nxt in graph[v]:
            if visited[nxt] ==0:
                visited[nxt]=cnt
                cnt +=1
                q.append(nxt)
        
    return visited

bfs(graph, R, visited)
print('\n'.join(map(str, visited[1:])))