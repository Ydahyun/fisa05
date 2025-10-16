
while True:

    N = input()

    if N == '0':
        exit()

    pandan=0

    for i in range(len(N)):
        if N[i] != N[len(N)-i-1]:
            pandan =1
            break
    if pandan == 1:
        print('no')
    else: print('yes')