M = int(input())
N = int(input())

output = []
for i in range(M, N+1):
    j = 1
    for j in range(1, i+1):
        j = j + 1
        if j == i:
            output.append(i)
        elif i % j == 0:
            break
if len(output) == 0:
    print(-1)
else:
    print(sum(output))
    print(min(output))
