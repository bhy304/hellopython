# 홀수와 짝수 구분
number = int(input("정수 입력> "))
# last_character = number[-1]
# last_number = int(last_character)

# <방법1>
# if last_number == 0 or last_number == 2 or last_number == 4 or last_number == 6 or last_number == 8:
#     print("짝수입니다.")

# if last_number == 1 or last_number == 3 or last_number == 5 or last_number == 7 or last_number == 9:
#     print("홀수입니다.")

# <방법2>
# if last_character in "02468":
#     print("짝수입니다.")

# if last_character in "13579":
#     print("홀수입니다.")

# <방법3>
if number % 2 == 0:
    print("짝수입니다.")

if number % 2 == 1:
    print("홀수입니다.")