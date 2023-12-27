N = int(input())
a = 0
while True:
    x = - 1/2 * N + 5/2 * a
    # print(f'a: {a}, x: {x}')
    if 0 <= x:
        if x <= a and x % 1 == 0:
            print(a)
            break
        elif a > N // 3:
            print(-1)
            break
    a += 1