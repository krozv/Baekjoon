# 10814 나이순 정렬
'''
회원들의 나이가 증가하는 순으로
나이가 같으면 먼저 가입한 사람이 앞에 오는 순서
'''
N = int(input())
member_list = []
for _ in range(N):
    age, name = input().split()
    age = int(age)
    member = [age, name]
    member_list.append(member)

member_list.sort(key=lambda x: (x[0]))
# print(member_list)
for member in member_list:
    print(*member)