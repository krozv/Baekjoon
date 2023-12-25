N = int(input())
input_data = list(map(int,input().split()))
output = 0
for i in range(N):
    for j in range(1, input_data[i]+1):
        j = j + 1
        if j == input_data[i]:
            output = output + 1
        elif input_data[i] % j == 0:
            break
print(output)
