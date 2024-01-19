import sys

data1 = []
for i in range(9):
    data1.append(list(map(int, sys.stdin.readline().split())))

# print(data1)
# print(len(data1))
data2 = []
for i in range(9):
    for j in range(9):
        data2.append(data1[i][j])
print(max(data2))
# print(data2.index(max(data2)))
max_index = data2.index(max(data2))
print(max_index//9 + 1, max_index % 9 + 1)
