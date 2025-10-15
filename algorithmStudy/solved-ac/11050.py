n,k=map(int, input().split())


bunja=1
bunmo=1
for i in range(k):
    bunja *= n-i

for i in range(1, k+1):
    bunmo *= i

print(int(bunja/bunmo))
