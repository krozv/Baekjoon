N, M = map(int, input().split())
case = []
for i in range (M):
    case.append(input())

basket = []

for i in range (N):
    basket.append(i+1)


for j in range (M):
    a, b = case[j].split()
    a = int(a)
    b = int(b)
    a_initial = basket[a-1]
    b_initial = basket[b-1]
    basket[a-1] = b_initial
    basket[b-1] = a_initial

for k in range (len(basket)):
    basket[k] = str(basket[k])

print(' '.join(basket))