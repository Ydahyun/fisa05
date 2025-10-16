import sys

input = sys.stdin.readline

while True:

    N = list(map(int, input().split()))

    if N[0] == 0 and N[1] == 0 and N[2] == 0:
        exit()

    pandan=0

    case1_1 = N[0]**2 + N[1]**2
    case1_2 = N[2]**2

    case2_1 = N[1]**2 + N[2]**2
    case2_2 = N[0]**2

    case3_1 = N[0]**2 + N[2]**2
    case3_2 = N[1]**2




    if case1_1 == case1_2 or case2_1 == case2_2 or case3_1 == case3_2:
        pandan =1


    if pandan == 1:
        print('right')
    else: print('wrong')