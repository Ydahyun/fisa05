# <문제> 음료수 얼려 먹기: 문제 설명
"""

"""

# 입력
"""

"""

# 출력
"""

"""

# 내 풀이 아이디어
"""



"""


# 동빈나 풀이
def dfs(x,y):
    
    if x <= -1 or x >= n or y <=-1 or y>=m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] =1
        
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n,m=map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
res=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            res+=1
print(res)
# Discussion
"""

"""