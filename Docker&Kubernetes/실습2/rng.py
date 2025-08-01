from random import randint

min_num = int(input("plz enter the min num: "))
max_num = int(input("plz enter the max num: "))

if max_num < min_num :
    print("invalid input - shutting down...")
else:
    rnd_num = randint(min_num, max_num)
    print(rnd_num)