# 별 찍기
input_data = int(input())
a = []
for i in range(1, input_data * 2):

    if i <= input_data:
        blank = input_data - i
        star = i * 2 - 1
    else:
        blank = i - input_data
        star = (input_data * 2 - 1) - 2 * blank

    output = ' ' * blank + '*' * star
    print(output)