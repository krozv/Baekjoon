A, B, V = map(int, input().split())
day_l = A - B
# 하루만에 올라가는 경우 V == A
if V == A:
    print(1)
# 딱 맞춰서 올라가는 경우 (V-A) % (A-B) == 0
elif ((V-A) % day_l) == 0:
    print((V-A) // day_l + 1)
# 한 번만 더 올라가면 끝인 경우 (V-A) % (A-B) != 0
else:
    print((V-A) // day_l + 2)