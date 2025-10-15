
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    apt = [ [1] for _ in range(k+1) ]  # 0층 포함 총 4 개 층

    for i in range(2, 14+1):
        apt[0].append(i)

    #print(apt)

    floor = 0
    for _ in range(k):
        for i in range(1, 14):
            apt[floor+1].append(apt[floor][i] + apt[floor+1][i-1])
            #print(apt)

        floor +=1

    print(apt[k][n-1])

