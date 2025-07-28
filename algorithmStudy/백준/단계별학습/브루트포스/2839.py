# 백준 2839번
# <문제> 설탕 배달: 문제 설명
"""

"""

#N = int(input())
N=21
result = -1

# 5kg 먼저 계산
for x in range(N // 5, -1, -1):  # 5로 나눈 최대 개수부터 줄여나가기
    remain = N - (5 * x)
    if remain % 3 == 0:
        y = remain // 3
        result = x + y
        break

print(result)