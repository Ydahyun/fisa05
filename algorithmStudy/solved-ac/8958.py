T = int(input())



for _ in range(T):
    res = []
    s = list(input())
    
    for _ in range(len(s)):
        res.append(0)

    if s[0] == 'O':
        res[0]=1
    else: res[0]=0

    for i in range(1, len(s)):
        if (s[i-1] == "O" and s[i]=="O") or s[i]=="O":
            res[i] = res[i-1] + 1
        elif s[i-1] == "X" and s[i]=="X":
            res[i] = 0

        
    print(sum(res))