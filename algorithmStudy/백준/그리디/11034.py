# 백준 11034번
# <문제> 문제제목: 문제 설명
"""
캥거루 세 마리가 사막에서 놀고 있다. 사막에는 수직선이 하나 있고, 캥거루는 서로 다른 한 좌표 위에 있다.

한 번 움직일 때, 바깥쪽의 두 캥거루 중 한 마리가 다른 두 캥거루 사이의 정수 좌표로 점프한다. 한 좌표 위에 있는 캥거루가 두 마리 이상일 수는 없다.

캥거루는 최대 몇 번 움직일 수 있을까?
"""

# 입력
"""
여러개의 테스트 케이스로 이루어져 있으며,
 세 캥거루의 초기 위치 A, B, C가 주어진다. 
 (0 < A < B < C < 100)

"""
#a b _ _ _ c
# 출력
"""
각 테스트에 대해 캥거루가 최대 몇 번 
움직일 수 있는지 출력한다.
"""

# 내 풀이 아이디어
"""
사이 간격이 넓은 곳으로 점프해야 이득임.
ex) a,b,c = 2,3,5
a와 b 사이 간격 구하는 식 1: b-a-1
c와 b 사이 간격 구하는 식 2: c-b-1 
식1과 식2 비교해서 작은 쪽이 캥거루 사이로 점프
점프는 그냥 가운데캥거루(b)바로 옆으로 이동시킬거임.
만약 식1이 작은경우 a의 위치는 b위치+1
반대의 경우) 식2이 작은경우 c의 위치는 b위치-1
같은 경우에는 상관없으니까 a(왼쪽)이동시킬게여
while문 돌리고 더이상 이동 못시키면 break로 탈출

"""
"""
# a,b,c=3,5,9

def solve(a, b, c):

    count = 0

    while True:

        equ1 = b-a-1 # >= 0 
        equ2 = c-b-1

        if (equ1==0) and (equ2==0):   # 더이상점프안되는경우
            break
        
        elif equ1 <= equ2:  # 같은 경우 고려해서 <=
            a,b,c = b,b+1,c
            count +=1
            
        elif equ1 > equ2:
            a,b,c = a,b-1,b
            count +=1

    # print(count)
    return count

if __name__ == '__main__':
    a,b,c = map(int, input().split())
    answer = solve(a, b, c)
    print(answer)
"""

"""
while 1:
    try:
        A, B, C = map(int, input().split())
        print(max(B-A, C-B)-1)
    except:
        break
    
import sys
for line in sys.stdin:
    a, b, c = map(int, line.split())
    print(max(b - a - 1, c - b - 1))
"""

a,b,c = map(int, input().split())
def dh(a, b, c):
    count = 0
    while True:
        equ1 = b-a-1
        equ2 = c-b-1
        if (equ1==0) and (equ2==0):   # 더이상점프안되는경우
            break
        elif equ1 <= equ2:  # 같은 경우 고려해서 <=
            a,b,c = b,b+1,c
            count +=1
        elif equ1 > equ2:
            a,b,c = a,b-1,b
            count +=1
    return count

# 최종종~
# 파이썬은 EOF처리를 못한다는 수업자료기억이나네..
try:
    while tmp := input():
        a,b,c = map(int, tmp.split())
        count = 0
        while True:
            equ1 = b-a-1 # >= 0
            equ2 = c-b-1
            if (equ1==0) and (equ2==0):   # 더이상점프안되는경우
                break
            elif equ1 <= equ2:  # 같은 경우 고려해서 <=
                a,b,c = b,b+1,c
                count +=1
            elif equ1 > equ2:
                a,b,c = a,b-1,b
                count +=1
        print(count)
except EOFError:
    pass