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

def U():  # 상
    if initial_locate[0] > 1:
        initial_locate[0] -= 1

def D():
    if initial_locate[0] < N:
        initial_locate[0] += 1

def L():
    if initial_locate[1] > 1:
        initial_locate[1] -= 1

def R():
    if initial_locate[1] < N:
        initial_locate[1] += 1

for i in move:
    match i:
        case "U":
            U()
        case "D":
            D()
        case "L":
            L()
        case "R":
            R()

print(initial_locate)

# 동빈나 풀이

n = 5
x,y=1,1
plans = ['R','R','R','U','D','D']
# L, R, U, D에 따른 이동방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]

move_types = ['L', "R", "U", "D"]

for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx>n or ny>n:
        continue
    # 이동수행
    x,y = nx, ny
    
print(x,y)