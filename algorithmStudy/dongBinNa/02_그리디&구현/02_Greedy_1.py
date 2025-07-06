# <문제> 1이 될 때까지: 문제 설명
"""
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다.
2. N을 K로 나눈다.

예) N=17, K=4일때, 과정 1. 한 번과 과정 2. 두 번을 수행하면 최적해

입력조건 
첫째 줄에서 N(1 <= N <= 100,000)과 K(2 <= K <= 100,000)가 공백을
기준으로 하여 각각 자연수로 주어집니다.

출력조건
첫째 줄에서 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는
횟수의 최솟값을 출력합니다.
"""

# 내 풀이
"""
내 풀이 아이디어
먼저 아무래도 N을 K로 나누는게 1로 가장 빨리 떨어지니까
N%K==0이 되는지 조사를 먼저하고,
되면 과정2로, 안되면 나누어 떨어질 때까지 과정1로 가기.
함수로 구현하면 될 듯
"""

N=25
K=3

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

# 동빈나 풀이

# N, K을 공백을 기준으로 구분하여 입력 받기
# n, k = map(int, input().split())
n=25
k=5
result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k) * k
    result += (n-target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break
    # K로 나누기
    result += 1
    n //= k
    
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)