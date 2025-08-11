from collections import deque
import sys

input = sys.stdin.readline
MAX = 100_000

graph = [0] * (MAX + 1)  # 0=미방문, 1=동생 위치 표시용
N, K = map(int, input().split())
graph[K] = 1

# N >= K면 뒤로 걷기만 하는 게 최단
if N >= K:
    print(N - K)
    sys.exit(0)

moves = [
    lambda x: x - 1,
    lambda x: x + 1,
    lambda x: x * 2,
]

visited = [False] * (MAX + 1)
q = deque([(N, 0)])
visited[N] = True

while q:
    x, d = q.popleft()
    for f in moves:
        nx = f(x)
        if 0 <= nx <= MAX and not visited[nx]:
            # "동생 자리를 1로 두고 1을 찾으면 끝" 로직
            if graph[nx] == 1:         # nx == K 와 동일
                print(d + 1)
                sys.exit(0)
            visited[nx] = True
            q.append((nx, d + 1))