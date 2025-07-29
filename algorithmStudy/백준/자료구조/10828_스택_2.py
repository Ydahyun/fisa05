# 백준 10828번
# <문제> 스택: 문제 설명

# 내 풀이 아이디어
"""
처음에 명령 몇 개를 받을건지 입력받고 반복문으로 아래거
push때문에 input().split()으로 받아야할듯
push일때 top, size, empty pop 조건문으로 분기나눠서 구현하면될듯
"""
import sys
input = sys.stdin.readline  # 빠른 입력

stk = []
res = []  # 출력 모아두기

N = int(input())

for _ in range(N):
    order = input().split()
    if order[0] == 'push':
        stk.append(int(order[1]))
    elif order[0] == 'pop':
        res.append(str(stk.pop()) if stk else '-1')
    elif order[0] == 'size':
        res.append(str(len(stk)))
    elif order[0] == 'empty':
        res.append('1' if not stk else '0')
    elif order[0] == 'top':
        res.append(str(stk[-1]) if stk else '-1')

# 한 번에 출력
print("\n".join(res))


# Discussion
"""

"""