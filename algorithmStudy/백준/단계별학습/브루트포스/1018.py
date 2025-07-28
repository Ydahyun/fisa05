# 백준 1018번
# <문제> 체스판 다시 칠하기: 문제 설명
"""
약간 스트라이드 느낌으로 가야할듯.
체스판 크기는 8*8
입력에 10 13으로 주어지는데,
행*열로, 10행 13열임.
N*M

그러면 8개씩 돌리니까
x축방향으로 이동하는건,
13-8해서 5번 움직이고.
y축방향으로 이동하는건,
10-8해서 1+2번 움직이는거야.
(1을 더한이유는 첫 줄때문에)


첫줄부터 5번움직이고,
한줄내려와서 또 5번 x축방향으로 이동,
마지막줄 내려와서 5번 x축방향으로 이동.
그러면 총 15번 반복하게되는거지.

x축방향으로 이동하는건,
for i in range(M-8):
    pass

y축방향으로 이동하는건,
for i in range(N-8+1):
    pass
    
이렇게 스트라이드 구현하면되고,

체커를 함수로 구현하면 좋을 것 같아.
첫 번째가 B이면 다음거는 W로 바꾸는형태.
i =   [0,1,2,3,4,5,6,7] 총 8번 시퀀스일때,
쳌 =  [B,W,B,W,B,W,B,W] 이렇게 되게끔
i가 짝수일땐 B인지 확인해서 B이면 그대로두고,
아니면 W로 바꿔주는거야. 그리고 카운트하고.

i가 홀수일땐 W인지 확인해서 W이면 그대로두고,
아니면 B로바꿔. 그리고 카운트

반대로 첫 번째가 W이면 다음거는 B로바꾸는형태인데
i =   [0,1,2,3,4,5,6,7] 총 8번 시퀀스일때,
쳌 =  [W,B,W,B,W,B,W,B] 이렇게 되게끔
i가 짝수일땐 W인지 확인해서 W이면 그대로두고,
아니면 B로 바꿔주는거야. 그리고 카운트하고.

i가 홀수일땐 B인지 확인해서 B이면 그대로두고,
아니면 W로바꿔. 그리고 카운트
"""

# input 파트

N, M= map(int, input().split())
input_list=[]
for _ in range(N):
    input_list.append(list(input()))
# print(input_list)
# 인풋파트 완료


def stride(N, M, input_list):
    cnt_list = []

    for j in range(N - 8 + 1):      # y축 방향
        for i in range(M - 8 + 1):  # x축 방향
            cnt1 = 0  # 시작이 B일 때 다시 칠해야 할 칸 수
            cnt2 = 0  # 시작이 W일 때 다시 칠해야 할 칸 수

            for y in range(8):
                for x in range(8):
                    current = input_list[j + y][i + x]
                    if (x + y) % 2 == 0:
                        if current != 'B': cnt1 += 1
                        if current != 'W': cnt2 += 1
                    else:
                        if current != 'W': cnt1 += 1
                        if current != 'B': cnt2 += 1

            cnt_list.append(min(cnt1, cnt2))

    return cnt_list


print(min(stride(N, M, input_list)))
