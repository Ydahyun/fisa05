# <문제> 1이 될 때까지: 문제 설명

"""
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

예) N=17, K=4일때, 과정 1. 한 번과 과정 2. 두 번을 수행하면 최적해
"""

N=17
K=4

def oper1(n):
    global N
    N = n-1
    return N

def oper2(n):
    global N
    global K
    N = int(N // K)
    return N

cnt = 0

while N != 1:
    if N%K == 0:
        oper2(N)
        cnt +=1
    else: 
        oper1(N)
        cnt +=1

print(cnt)