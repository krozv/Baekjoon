num1 = list(input())
num2 = list(input())

list1, list2 = [], []
for i in range(len(num1)):
    list1.append(int(num1[i]))
    list2.append(int(num2[i]))

num3, num4, num5 = 0, 0, 0
for i in range(len(num1)):
    num3 = num3 + (list1[i] * list2[-1] * 10**(len(num1)-1-i))
    num4 = num4 + (list1[i] * list2[-2] * 10**(len(num1)-1-i))
    num5 = num5 + (list1[i] * list2[-3] * 10**(len(num1)-1-i))

num6 = int(num3 + num4*1e1 + num5*1e2)
print(num3, num4, num5, num6, sep='\n')