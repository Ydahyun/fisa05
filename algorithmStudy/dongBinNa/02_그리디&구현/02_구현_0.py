# <문제> 상하좌우: 문제 설명
"""
여행가 A는 N*N 크기의 정사각형 공간 위에 서있다.
이 공간은 1*1 크기의 정사각형으로 나누어져있다.
가장 왼쪽 위 좌표는 1,1이며 가장 오른쪽 좌표는 N,N이다.
시작좌표는 항상 1,1이며 상하좌우(UDLR)로 이동한다.

행은 세로방향, 열은 가로방향으로 표시한다.

(1,1) | (1,2) | ... | (1,5)
(2,1) |
 ...  |
(5,1) |

"""

# 내 풀이
"""
내 풀이 아이디어
그냥 구현하면 되는거다.

"""

N = 5
move = ['R','R','R','U','D','D']
initial_locate = [1,1]

def U(n):  # 상
    global initial_locate
    if initial_locate[0] > 1:
        return initial_locate[0] + 1

def D(n):
    global initial_locate
    if initial_locate[0] < N:
        return initial_locate[1] + 1

def L(n):
    global initial_locate
    if initial_locate[1] > 1:
        return initial_locate[1] + 1

def R(n):
    global initial_locate
    if initial_locate[1] < N:
        return initial_locate[1] + 1

for i in move:
    match i:
        case "U":
            U(i)
        case "D":
            D(i)
        case "L":
            L(i)
        case "R":
            R(i)

print(initial_locate)
    



# 동빈나 풀이
