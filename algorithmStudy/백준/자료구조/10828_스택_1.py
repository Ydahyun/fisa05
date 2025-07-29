# 백준 10828번
# <문제> 스택: 문제 설명

# 내 풀이 아이디어
"""
처음에 명령 몇 개를 받을건지 입력받고 반복문으로 아래거
push때문에 input().split()으로 받아야할듯
push일때 top, size, empty pop 조건문으로 분기나눠서 구현하면될듯
"""
stk=[]

N=int(input())

for _ in range(N):
    order=input().split()
    if order[0] == 'push':
        stk.append(int(order[1]))
    elif order[0] == 'pop':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif order[0] == 'size':
        print(len(stk))
    elif order[0] == 'empty':
        if len(stk)==0:
            print(1)
        else: print(0)
    elif order[0] == 'top':
        if len(stk)==0:
            print(-1)
        else:
            print(stk[-1])


# Discussion
"""

"""