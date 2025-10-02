a_li = []

for _ in range(9):
    a_li.append(int(input()))

print(max(a_li))
print(a_li.index(max(a_li))+1)