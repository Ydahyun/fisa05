ac = [1,2,3,4,5,6,7,8]
dc = [8,7,6,5,4,3,2,1]

T = list(map(int, input().split()))


if ac == T:
    print("ascending")
elif dc == T:
    print("descending")
else:
    print("mixed")