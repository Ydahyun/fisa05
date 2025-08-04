import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

N, M, R = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

#print(adj)
for neighbours in adj:
    neighbours.sort(reverse=True)          # 내림차순
#print(adj)

visited=[0]*(N+1)
cnt=1

def DFS(graph, v, visited):
    global cnt
    visited[v] = cnt  # 현재 노드를 방문 처리
    cnt +=1

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if visited[i]==0:
            DFS(graph, i, visited)

DFS(adj, R, visited)
# print(visited)
print('\n'.join(map(str, visited[1:])))