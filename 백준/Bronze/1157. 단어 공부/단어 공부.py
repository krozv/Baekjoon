input_data = list(input())
upper_input = []
count_input = []
# input의 알파벳을 전부 large로 변경
for i in range (len(input_data)):
    upper_input.append(input_data[i].upper())
# print(upper_input)

# 사용된 알파벳 리스트 형성
upper_input.sort()
used_alphabet = list(set(upper_input))

# 알파벳마다 사용횟수 count_input 리스트에 작성
for j in range (len(used_alphabet)):
    count_input.append(upper_input.count(used_alphabet[j]))
Max = max(count_input)

# output
if count_input.count(Max) > 1:
    print('?')
else:
    print(used_alphabet[count_input.index(Max)])