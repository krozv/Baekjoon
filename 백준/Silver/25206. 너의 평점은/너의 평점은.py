# 너의 평점은
def total_score(credit, grade):
    if grade == 'A+':
        score = 4.5
    elif grade == 'A0':
        score = 4.0
    elif grade == 'B+':
        score = 3.5
    elif grade == 'B0':
        score = 3.0
    elif grade == 'C+':
        score = 2.5
    elif grade == 'C0':
        score = 2.0
    elif grade == 'D+':
        score = 1.5
    elif grade == 'D0':
        score = 1.0
    elif grade == 'F':
        score = 0.0
    elif grade == 'P':
        score = 100
    sum = score * credit
    return sum


total = []
total_credit = []
while True:
    try:
        subj, input_credit, input_grade = input().split()
        input_credit = float(input_credit)
        
        if input_grade == "P":
            input_credit = 0
        
        total.append(total_score(input_credit,input_grade))
        total_credit.append(input_credit)
    except:
        break

print(sum(total)/sum(total_credit))