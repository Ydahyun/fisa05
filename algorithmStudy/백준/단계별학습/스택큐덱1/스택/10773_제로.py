import sys

input = sys.stdin.readline

K = int(input().strip())
stk = []
for _ in range(K):
    n= int(input().strip())
    if n == 0:
        stk.pop()
    else:
        stk.append(n)
print(sum(stk))