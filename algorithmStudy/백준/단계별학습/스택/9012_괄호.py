import sys

input = sys.stdin.readline

T = int(input())#.strip())

for _ in range(T):
    stk = []
    S = input().strip()
    S_li = list(S)
    #print(S_li)
    for i in range(len(S_li)):
        if len(stk)==0:
            stk.append(S_li[i])
            continue
        elif stk[-1] == S_li[i]:
            stk.append(S_li[i])
        elif stk[-1] != S_li[i]:
            if (stk[-1]=='(' and S_li[i]==')'):
                stk.append(S_li[i])
                stk.pop()
                stk.pop()
            else: stk.append(S_li[i])
    #print(stk)
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