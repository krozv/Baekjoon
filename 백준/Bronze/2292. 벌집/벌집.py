N = int(input())
bee = True
i = 0
num = 1
while bee:
    num = num + 6 * i
    i += 1
    if N <= num:
        bee = False
print(i)