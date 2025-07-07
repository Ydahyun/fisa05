import sys
input = sys.stdin.readline

while True:
    try:
        # 입력
        A, B, C = map(int, input().split())

        # 간격이 넓은 곳으로 착지
        print(max(B-A, C-B)-1)
    except:
        break