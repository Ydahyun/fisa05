from collections import deque

N, K = map(int, input().split())

graph = [0 for _ in range(0, 100_000+1)]
# print(len(graph))# 100_001

cnt=0

def bfs(graph, x, y):
    queue = deque()
    queue.append(x)
    global cnt

    while queue:

        x = queue.popleft()
        #4  
        dx=[-1,1,x]
        for i in range(3):
            nx = x + dx[i]
            # cnt +=1

            # 이탈하면 컨티뉴
            if nx <0 or nx >1e5:
                continue
            
            else:
                queue.append(nx)
                graph[nx] = graph[x] + 1
            if nx == y:
                break
    return graph[nx]
                
print(bfs(graph, N-1, K-1))