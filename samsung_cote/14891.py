# N극은 0, S극은 1
# 톱니의 이는 8개이다.
# 12시 방향부터 시계 방향 순서대로 주어짐.
# SNSN SSSS -> 1010 1111

# 시계방향 1, 반시계 방향 -1


# 맞닿는 인덱스는 2-6

# 돌리기 전 상태에서 맞닿은 부분에 대하여
# 같으면 회전x, 다르면 회전
# 회전 시킬 때, 데큐로 넣었다 뺏다 하면 좋을 것같은데
# popleft(), pop(), appendleft(), append()

# 입력부

from collections import deque

# 데큐 완성
q = deque()
for _ in range(4):
    q.append(list(map(int, input())))

# 몇 번 돌릴건 지 받는 변수
rot = int(input())
sol = 0  # 솔루션

# 맞물리는게 같은지 다른지 확인하는 함수
def checker(q):
    check1, check2, check3 = False, False, False
    # 첫 바퀴와 둘째바퀴 같은지 확인
    # check1으로 명명
    if q[0][2] == q[1][6]:
        check1 = True
    # 둘째바퀴와 셋째바퀴 같은지 확인
    # check2으로 명명
    if q[1][2] == q[2][6]:
        check2 = True
    # 셋째바퀴와 넷째바퀴 같은지 확인
    # check3으로 명명
    if q[2][2] == q[3][6]:
        check3 = True
    
    return check1, check2, check3


# 같으면 회전x, 다를 때 회전
# 시계 방향 회전
def rot_cw(q, x):
    q[x].appendleft(q[-1])
    q[x].pop()

    return q
# 반시계 방향 회전
def rot_ccw(q, x):
    q[x].append(q[0])
    q[x].popleft()

    return q


for _ in range(rot):
    # x는 회전 시킬 톱니바퀴의 번호
    # y는 방향; 시계방향: 1, 반시계: -1
    x, y = map(int, input().split())
    
    # 함수로 구현해야 할 듯
    # 데큐는 있으니까
    # 먼저 맞물리는거 체크를 해
    check1, check2, check3 = checker(q)

    # 그리고 해당하는 x번째 바퀴를 일단 돌려
    if y == 1:  # 시계방향
        rot_cw(q, x)
    else:       # 반시계방향
        rot_ccw(q, x)

    if x == 1 and not check1:
        if y == 1:
            rot_ccw(q, 1)
        else:
            rot_cw(q, 1)
    
    if x == 2 and (not check1):
        if y == 1:
            rot_ccw(q,0)
        else:
            rot_cw(q,0)
    if x == 2 and (not check2):
        if y == 1:
            rot_ccw(q,2)
        else:
            rot_cw(q,2)

    if x == 3 and (not check2):
        if y == 1:
            rot_ccw(q,1)
        else:
            rot_cw(q,1)
    if x == 3 and (not check3):
        if y == 1:
            rot_ccw(q,3)
        else:
            rot_cw(q,3)

    if x == 4 and not check3:
        if y == 1:
            rot_ccw(q, 2)
        else:
            rot_cw(q, 2)

print(q)