from collections import deque

import sys

input = sys.stdin.readline

graph = []

N, M = map(int, input().split())
# print(N, M)

# 방 만들기
for i in range(N+1):
    graph.append([])
# print(graph)

# 값 넣기
for i in range(M):
    idx, val = map(int, input().split())
    graph[idx].append(val)
    graph[val].append(idx)

#print(graph)

######## 그래프 완료!! ########
"""
[[], 
 [2, 5], 
 [1, 5], 
 [4], 
 [3, 6], 
 [2, 1], 
 [4]]
"""
visited = [False]*(N + 1)
# print(visited)
def BFS(x):
    queue = deque()
    queue.append((x))
    visited[x] = True

    while queue:
        x = queue.popleft()

        for i in range(len(graph[x])):
            if visited[graph[x][i]] == True:
                continue
            
            queue.append(graph[x][i])
            visited[graph[x][i]] = True

# BFS(1)

cnt = 0
for i in range(1, N + 1, 1):
    if visited[i] == True:
        continue
    BFS(i)
    cnt += 1


print(cnt)