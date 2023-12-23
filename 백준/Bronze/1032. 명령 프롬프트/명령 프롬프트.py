import sys

N = int(input())
data = []

for i in range(N):
    data.append(list(sys.stdin.readline()))

output = []
if N == 1:
    output = data[0]
    print(''.join(output))
else:
    for i in range(len(data[0])-1):
        for j in range(N-1):
            if data[j][i] != data[j+1][i]:
                if len(output) == i:
                    output.append('?')
                break
            else:
                if j == N-2:
                    output.append(data[j][i])
    print(''.join(output))