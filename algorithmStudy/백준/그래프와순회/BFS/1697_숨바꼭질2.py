from collections import deque
import sys

input = sys.stdin.readline

graph = [0] * (100_000 + 1)  # 전체 맵

N, K = map(int, input().split())

graph[K] = 1  # 동생이 있는 위치를 1로 채워줌
cnt =0 
def bfs(N, K):

    # 뒤로 걷기만 하면 되는 경우 빠른 처리
    if N >= K:
        return N - K

    queue=deque()
    queue.append((N, 0))  # 최초 수빈이의 위치를 큐에 넣어줌
    global cnt
    nx = N

    dx = [
        lambda x: x - 1,
        lambda x: x + 1,
        lambda x: 2 * x
    ]

    while queue:
        
        x, d = queue.popleft()
      
        # for i in range(3):
        for f in dx:
            nx = f(x)
           
            if nx <0 or nx>=len(graph):
                continue
            else: 
                queue.append((nx , d + 1))

        cnt +=1
        if graph[nx] == graph[K]:
            break
    print(cnt)
            
bfs(N)