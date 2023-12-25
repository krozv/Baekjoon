import sys
input_data = True
test = []

while input_data:
    a, b = map(int, (sys.stdin.readline().split()))
    if a == 0:
        input_data = False
        break
    test.append([a, b])
    # print(test)

output = []
for i in range (len(test)):
    if test[i][0] % test[i][1] == 0:
        print("multiple")
    elif test[i][1] % test[i][0] == 0:
        print("factor")
    else:
        print("neither")