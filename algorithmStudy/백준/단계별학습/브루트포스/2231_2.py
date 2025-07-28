# 백준 2231번
# <문제> 분해합: 문제 설명

N = int(input())
result = 0

# 생성자 후보: max(1, N - 9 * 자리수길이) ~ N까지
for i in range(max(1, N - 9 * len(str(N))), N):
    digit_sum = sum(map(int, str(i)))  # 각 자리수 합
    if i + digit_sum == N:
        result = i
        break

print(result)
