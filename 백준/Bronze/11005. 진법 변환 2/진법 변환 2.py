N, A = map(int, input().split())
output = []
B = []
while True:
    output.append(N % A)
    if N < A:
        break
    N = N // A
output.reverse()
for i in range(len(output)):
    if output[i] >= 10:
        B.append(chr(output[i]+55))
    else:
        B.append(str(output[i]))
print(''.join(B))


