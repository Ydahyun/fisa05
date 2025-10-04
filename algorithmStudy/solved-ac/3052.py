li=[]
for _ in range(10):
    a = int(input())
    li.append(a)

sol=[]
for i in range(10):
    if li[i] % 42 !=0:
        sol.append(li[i] % 42)
    else: sol.append(0)
s_s=set(sol)

print(len(s_s))