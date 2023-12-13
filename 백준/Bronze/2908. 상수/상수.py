a, b = input().split()

a_list = list(a)
b_list = list(b)
a_list.reverse()
b_list.reverse()

a = int(''.join(a_list))
b = int(''.join(b_list))

if a > b:
    print(a)
else:
    print(b)
