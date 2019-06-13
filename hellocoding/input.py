# 입력
# input() 함수 -> 문자열이 나옴

# print("입력된 데이터 자료: ", string)
# print("입력된 데이터 자료형: ", type(string))

string_a = input("입력A> ") 
int_a = int(string_a)

string_b = input("입력B> ") 
int_b = int(string_b)

print("문자열 자료: ", string_a + string_b) # 문자열 연결
print("숫자 자료: ", int_a + int_b)