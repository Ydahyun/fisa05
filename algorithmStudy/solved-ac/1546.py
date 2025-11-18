N = int(input())
sc_list = list(map(int, input().split()))

max_sc = max(sc_list)
new_avg = sum((sc / max_sc) * 100 for sc in sc_list) / N

print(new_avg)
