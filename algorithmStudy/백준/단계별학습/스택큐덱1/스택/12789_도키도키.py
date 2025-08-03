import sys

input = sys.stdin.readline

N = int(input())

line = input().rstrip().split()

line = list(map(int, line))
# print(line)
stk = []
pass_li=[]
# 2 1 3

stk.append(line[0])
del line[0]
#print(line)

# [3]
# [1 2  ]
for i in range(len(line)):  # len(stk) 해서 계속 안된거였다..
    if stk[-1]>line[i]:
        stk.append(line[i])
        #print(stk)
    elif stk[-1]<line[i]:
        
        while True:
            if len(stk)==0:
                stk.append(line[i])
                break
            elif stk[-1]<line[i]:
                pass_li.append(stk[-1])
                stk.pop()
                #
                #print(stk)
            else:
                stk.append(line[i])
                break
        
for i in range(len(stk)):
    pass_li.append(stk.pop())

#print(pass_li)
flag=True
for i in range(len(pass_li)-1):
    if pass_li[i] < pass_li[i+1]:
        continue
    else: 
        print("Sad")
        exit()
if flag: print("Nice")