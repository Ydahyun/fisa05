N = int(input())

a = list(map(int, input().split()))
cnt=0
for i in range(N):
    if a[i] ==1:
        continue
    for j in range(2, a[i]):
        if a[i] % j == 0:
            break
    else: cnt +=1
print(cnt)