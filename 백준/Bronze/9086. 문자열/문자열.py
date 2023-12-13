T = int(input())
case = []
for i in range(T):
    case.append(input())

output = []
for j in range(T):
    test = list(case[j])
    print(test[0] + test[-1])
