list_number = [52, 273, 32, 72, 100]
# try except 구문으로 예외를 처리합니다.
# try:
#     # 숫자를 입력 받는다.
#     number_input_a = int(input("정수 입력> "))
#     # 리스트의 요소 출력
#     print("{}번째 요소: {}".format(number_input_a, list_number[number_input_a]))
# except Exception as exception:
#     # 예외 객체 출력
#     print("type(exception): ",type(exception))
#     print("exception: ", exception)
#     if type(exception) == IndexError:
#         print("인덱스를 넘었습니다. 5 미만의 값을 입력해주세요.")
#     elif type(exception) == ValueError:
#         print("정수를 입력해주세요!")
#     else:
#         print("알 수 없는 예외가 발생했습니다.")

try:
    number_input_a = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input_a, list_number[number_input_a]))
except IndexError as exception:
    print("5 미만의 값을 입력해주세요.")
except ValueError as exception:
    print("정수를 입력해주세요!")
except Exception as exception:
    print("예상하지 못한 예외가 발생했습니다.")