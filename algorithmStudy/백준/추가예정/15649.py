import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())

for p in permutations(range(1, n + 1), m):
    print(*p)
