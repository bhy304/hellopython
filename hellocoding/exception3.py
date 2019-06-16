input_a = input("정수 입력> ")
if input_a.isdigit():
    number_input_a = int(input_a)
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if number_input_a < len(list_a):
        print(list_a[number_input_a])
    else:
        print("리스트의 범위를 넘습니다.")
else:
    print("프로그램을 종료합니다.")