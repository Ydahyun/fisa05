# 백준 28278번
# <문제> 스택2: 문제 설명

# 내 풀이 아이디어
"""

"""
import sys
input = sys.stdin.readline  # 빠른 입력

N = int(input())

#a = int(sys.stdin.readline())         # '123\n' → int('123\n') 에러 (공백 제거 필요)
#a = int(sys.stdin.readline().strip()) # '123\n' → '123' → int('123') OK


stk = []

for _ in range(N):
    order = input().split()
    if order[0] == '1':
        stk.append(int(order[1]))
    elif order[0] == '2':
        if len(stk) == 0:
            print(-1)
        else: print(stk.pop())
    elif order[0] == '3':
        print(len(stk))
    elif order[0] == '4':
        if len(stk) == 0:
            print(1)
        else: print(0)
    elif order[0] == '5':
        if len(stk) != 0:
            print(stk[-1])
        else: print(-1)


# Discussion
"""

"""