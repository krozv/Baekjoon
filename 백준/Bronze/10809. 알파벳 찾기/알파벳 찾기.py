S = list(input())
alp = []
for i in range(ord('a'), ord('z')+1):
    alp.append(chr(i))
    # print(alp)

for j in range(len(alp)):
    if alp[j] in S:
        alp[j] = str(S.index(alp[j]))
    elif alp[j] not in S:
        alp[j] = str(-1)

print(' '.join(alp))