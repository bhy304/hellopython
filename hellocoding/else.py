# else 구문
'''
if <불 값>:
    <참일 때 실행할 문장>
else:
    <거짓일 때 실행할 문장>
'''
number = input("정수 입력> ")
number = int(number)

if number % 2 == 0:
    # 참일 때
    print("{}는 짝수입니다.".format(number))
else:
    # 거짓일 때
    print("{}는 홀수입니다.".format(number))