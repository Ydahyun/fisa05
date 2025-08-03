import sys

input = sys.stdin.readline

while True:
    S = input().rstrip()
    if S == '.':
        break   

    stk = []
    flag = True
    
    # stk가 비어있으면 False 반환
    for ch in S:
        if ch == '(' or ch == '[':
            stk.append(ch)
        elif ch == ')':
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                flag = False
                break
        elif ch == ']':
            if stk and stk[-1] == '[':
                stk.pop()
            else:
                flag = False
                break

    if flag and not stk:
        print('yes')
    else:
        print('no')
