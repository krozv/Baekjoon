N, B = input().split()
N = list(N)
B = int(B)

str_data = []
i = 0
for i in range(36):
    if i <= 9:
        str_data.append('')
    else:
        str_data.append(chr(i+55))
    i += 1

num = 0
output = 0
for i in range(len(N)):
    if N[i] in str_data:
        num = str_data.index(N[i]) * (B ** (len(N)-i-1))
    else:
        num = int(N[i]) * (B ** (len(N)-i-1))
    output += num

print(output)