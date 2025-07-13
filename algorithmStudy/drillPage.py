import sys
import heapq

def solve():
    # ↓ 빠른 입력
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))

    # 1️⃣ prefix 배열 생성
    prefix = []
    s = 0
    for a in A:
        s += a
        prefix.append(s)

    # 2️⃣ 가장 큰 K개 합산 ─ 두 가지 방법
    # 방법 A. 정렬 (N log N)
    # answer = sum(sorted(prefix, reverse=True)[:K])

    # 방법 B. heapq (N log K)  ← K가 훨씬 작을 수도 있으므로 보편적으로 안전
    largest_k = heapq.nlargest(K, prefix)  # max-heap 없이도 내부에서 알아서 정렬
    answer = sum(largest_k)

    print(answer)

if __name__ == "__main__":
    solve()
