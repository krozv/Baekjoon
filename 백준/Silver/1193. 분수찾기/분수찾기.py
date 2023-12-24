X = int(input())

order = True
i = 0
total = 0
while order:
    i = i + 1
    total = total + i
    # print(total)
    if total >= X:
        order = False
        # print(f"last order: {i}")

# 분모 + 분자 = i + 1
if i % 2 == 1:
    a = 1
    b = i
    for j in range(total-X):
        a = a + 1
        b = b - 1
    # 분자 감소, 분모 증가
else:
    a = i
    b = 1
    for j in range(total-X):
        a = a - 1
        b = b + 1
    # 분자 증가, 분모 감소
print(f"{a}/{b}")