# 고급 예외 처리
# try exception 구문

'''
try:
    <예외가 발생할 가능성이 있는 코드>
except:
    <예외가 발생했을 때 실행할 코드>
else:
    <예외가 발생하지 않았을 때 실행할 코드>
finally:
    <무조건적으로 실행할 코드>
'''
try:
    input_a = input("숫자 입력> ")
    number_input_a = int(input_a)
    print(number_input_a * number_input_a)
except:
    print("예외가 발생했습니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("반드시 실행되는 코드입니다.")