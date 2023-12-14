import sys

n, m = map(int, input().split())
# a = int(sys.stdin.readline())
data1 = []
for i in range(n):
    data1.append(list(map(int, sys.stdin.readline().split())))

data2 = []
for i in range(n):
    data2.append(list(map(int, sys.stdin.readline().split())))

output = []

for i in range(n):
    for j in range(m):
        output.append(str(int(data1[i][j]) + int(data2[i][j])))
        if j != m-1:
            output.append(' ')
    output.append('\n')
print(''.join(output))