# 나머지
example= []

# input을 list에 저장
for i in range (10):
    example.append(int(input()))


# print(example)
rest_list = []
for j in range(10):
    rest = example[j] % 42
    if rest not in rest_list:
        rest_list.extend([rest])
    # print(rest_list)

print(len(rest_list))