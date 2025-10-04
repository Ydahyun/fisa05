a = int(input())
b = int(input())
c = int(input())

d = a*b*c
d_str=str(d)
#print(d)
#dic = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
li = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(d_str)):
    li[int(d_str[i])] = li[int(d_str[i])] + 1

for i in range(0, len(li)-1):
    print(li[i])