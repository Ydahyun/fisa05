N = int(input())

if N == 1:
    print(1)
else:
    end = 1     # 현재 층의 마지막 번호
    k = 1       # 층(지나는 방 개수)
    while end < N:
        end += 6 * k
        k += 1
    print(k)