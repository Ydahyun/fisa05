import sys

input = sys.stdin.readline

T = int(input())#.strip())

for _ in range(T):
    stk = []
    S = input().split()
    
    print(S)
    for i in range(len(S)):
        print(i, stk)
        if len(stk)==0:
            stk.append(S[i])
            continue
        elif stk[i-1] == stk[i]:
            stk.append(S[i])
        elif stk[i-1] != stk[i]:
            stk.pop()
            stk.pop()
    if len(stk)==0:
        print('YES')
    else: print('NO')



    #if S 가 VPS면 print YES
    #else: print NO

"""
stack = []

while stack:
    if ~~
    else~~~
    stack.pop()
    stack.append()
"""