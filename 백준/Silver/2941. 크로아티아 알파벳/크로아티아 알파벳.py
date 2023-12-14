# 크로아티아 알파벳
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input_data = input()
a = 0

# croatia alphabet 유무를 확인 후, input에서 제거 & 제거한 횟수 변수a에 저장
for i in range(len(croatia)):
    if input_data.count(croatia[i]) != 0:
        # print(input_data.count(croatia[i]))
        a += int(input_data.count(croatia[i]))
        input_data = input_data.replace(croatia[i], "/")
        # print(input_data)
        
print(len(input_data)-int(input_data.count('/')) + a)