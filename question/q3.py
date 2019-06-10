# 아래 코드를 한 줄로 코딩하면 ?

# if int(score) > 50 :
#    grade = 'pass'
# else :
#    grade = 'fail'
# print(grade)

score = input("점수를 입력하세요>> ")
grade = "pass" if int(score) > 50 else "fail"
c