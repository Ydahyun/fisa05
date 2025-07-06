# 대표예제
# 거스름 돈

# 문제조건
# N을 입력 받고
# 화폐단위가 [500, 100, 50, 10]원인 동전으로 거슬러 주기
# 몇 개로 거슬러주는게 최적해?

# N = int(input("N = "))

N=1260

list_won = [500, 100, 50, 10]
cnt = 0
for i in list_won:
    if N == 0:
        break
    else:
        jandon_cnt = N // i
        N = N - (jandon_cnt) * i
        cnt += jandon_cnt

print(cnt)

# 동민나 풀이

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin

print(count)