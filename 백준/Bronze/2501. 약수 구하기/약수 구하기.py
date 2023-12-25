N, K = map(int, input().split())
factor = []
end_point = True
i = 0
while end_point:
    i = i + 1
    if i == N:
        factor.append(i)
        # print(factor)
        end_point = False
        break
    elif N % i == 0:
        factor.append(i)
        # print(factor)

if len(factor) >= K:
    print(int(factor[K-1]))
else:
    print(0)