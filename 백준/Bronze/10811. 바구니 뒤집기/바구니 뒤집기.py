# 바구니 뒤집기
N, M = map(int, input().split())

case = []
for i in range (M):
    case.append(input())

basket = []
for j in range (N):
    basket.append(j+1)
# print(basket)
rev_basket = []
for k in range (M):
    start, end = map(int, case[k].split())
    # print(start, end)
    rev_basket = basket[start-1:end]
    rev_basket.reverse()
    basket[start-1:end] = rev_basket

for l in range (len(basket)):
    basket[l] = str(basket[l])

print(' '.join(basket))

