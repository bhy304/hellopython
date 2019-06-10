# 아래의 코드를 dictionary를 사용해서 두줄로 코딩해보세요.
# score = input("점수를 입력하세요>> ")
# score = int(score)
# if score == 100 :
#    grade = 'A+'
# elif score  < 100 and score >=90 :
#    grade = 'A'
# elif score >= 80 :
#    grade = 'B'
# elif score >=70 :
#    grade  = 'C'
# elif score >= 60 :
#    grade = 'D'
# else :
#    grade = 'F '
# print(grade)

score = input("점수를 입력하시오>> ")
grade_score = {10:'A+',9:'A',8:'B',7:'C',6:'D'}
grade = grade_score.get(int(score) // 10, 'F')
print(grade)