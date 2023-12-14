a = list(input())
origin_a = []
for i in range(len(a)):
    origin_a.append(a[i])
a.reverse()
if a == origin_a:
    print(1)
else:
    print(0)