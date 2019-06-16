# 기본 예외 처리
# 예외 : 실행 중에 발생하는 오류
# 실행 중에 발생하는 오류를 미리 처리하는 것 : 예외처리
# - 기본예외처리 : if 등의 기본적인 방법으로 처리
# - 고급예외처리 : try exception 구문 사용

while True:
    input_a = input("정수 입력> ")
    if input_a.isdigit():
        number_input_a = int(input_a)
        print("원의 반지름: ", number_input_a)
        print("원의 둘레: ", 2 * 3.14 * number_input_a)
        print("원의 반지름: ", 3.14 * number_input_a * number_input_a)
        break
    else:
        print("정수를 입력해주세요!!!")