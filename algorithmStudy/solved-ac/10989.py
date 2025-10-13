import sys

input = sys.stdin.readline


N = int(input())

count = [0] * 10001  # 1~10,000니까 인덱스를 1로 맞춰주기위해서 10001

# N개의 정수를 인덱스로 생각해서 개수로 넣어
for _ in range(N):
    num = int(input())
    count[num] += 1

# 리스트에 저장된 개수만큼 인덱스를 출력
for i in range(10001):
    # count[i]이 1 이상이라면
    if count[i] != 0:
        # 그 값만큼 출력
        for j in range(count[i]):
            print(i)